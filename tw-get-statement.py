#!/usr/bin/env python3
"""Get statement for borderless currency.

Usage:
  tw-get-statement.py <currency> [--days=<days>]

Options:
  -h --help      Show this screen.
  --days=<days>  Number of days of history to return  [default: 30]

"""

SERVER = 'https://transferwise.com/gateway'

import requests
from datetime import datetime, timedelta
import pytz
import tempfile
import csv
import prettytable
from docopt import docopt
from _auth import API_TOKEN

arguments = docopt(__doc__, version='tw-get-statement 1.0')

assert API_TOKEN != 'XXXXXXX-XXXX-XXXX-XXXXXX'

# Get the list of profiles
list_profiles_response = requests.get(
    f'{SERVER}/v1/profiles',
    headers={'Authorization': f'Bearer {API_TOKEN}'},
)

# List the borderless accounts for the personal profile
profileId = list_profiles_response.json()[0]['id'] # Assume first profile returned is personal profile
list_accounts_response = requests.get(
    f'{SERVER}/v1/borderless-accounts',
    params={
        'profileId': profileId
    },
    headers={'Authorization': f'Bearer {API_TOKEN}'},
)
accountId = list_accounts_response.json()[0]['id']

# Download the statement for the balance in the chosen currency
currency = arguments['<currency>']
date_now = datetime.utcnow()
date_x_days_ago = date_now - timedelta(days=int(arguments['--days']))
download_statement_response = requests.get(
    f'{SERVER}/v1/borderless-accounts/{accountId}/statement.csv',
    params={
        'currency': currency,
        'intervalStart': date_x_days_ago.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'intervalEnd': date_now.strftime('%Y-%m-%dT%H:%M:%SZ')
    },
    headers={'Authorization': f'Bearer {API_TOKEN}'},
)

# Parse the CSV output and output a table with the desired columns
output = prettytable.PrettyTable()
output.field_names = ["Date", "Amount", "Description", "Running Balance"]
output.align["Description"] = "l"

csv_content = download_statement_response.content.decode('utf-8').splitlines()
csv_parser = csv.reader(csv_content, delimiter=',', quotechar='"')
next(csv_parser, None)  # skip the header row
for row in csv_parser:
    if (len(row) > 7):
        output.add_row([row[1], row[2], row[4], row[6]])

print(f'{currency} activity since {date_x_days_ago.strftime("%Y-%m-%d %H:%M:%S")}')
print(output)
