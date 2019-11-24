#!/usr/bin/env python3

SERVER = 'https://transferwise.com/gateway'
API_TOKEN='XXXXXXX-XXXX-XXXX-XXXXXX'
CURRENCY='EUR'

import requests
from datetime import datetime, timedelta
import pytz
import tempfile
import csv
import prettytable

list_profiles_response = requests.get(
    f'{SERVER}/v1/profiles',
    headers={'Authorization': f'Bearer {API_TOKEN}'},
)

profileId = list_profiles_response.json()[0]['id'] # Assume first profile returned is personal profile
list_accounts_response = requests.get(
    f'{SERVER}/v1/borderless-accounts',
    params={
        'profileId': profileId
    },
    headers={'Authorization': f'Bearer {API_TOKEN}'},
)

accountId = list_accounts_response.json()[0]['id']
date_now = datetime.utcnow()
date_x_days_ago = date_now - timedelta(days=30)

download_statement_response = requests.get(
    f'{SERVER}/v1/borderless-accounts/{accountId}/statement.csv',
    params={
        'currency': CURRENCY,
        'intervalStart': date_x_days_ago.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'intervalEnd': date_now.strftime('%Y-%m-%dT%H:%M:%SZ')
    },
    headers={'Authorization': f'Bearer {API_TOKEN}'},
)

csv_content = download_statement_response.content.decode('utf-8').splitlines()
csv_parser = csv.reader(csv_content, delimiter=',', quotechar='"')

output = prettytable.PrettyTable()
output.field_names = ["Date", "Amount", "Description", "Running Balance"]
output.align["Description"] = "l"

next(csv_parser, None)  # skip the headers
for row in csv_parser:
    if (len(row) > 7):
        output.add_row([row[1], row[2], row[4], row[6]])

print(f'{CURRENCY} activity since {date_x_days_ago.strftime("%Y-%m-%d %H:%M:%S")}')
print(output)
