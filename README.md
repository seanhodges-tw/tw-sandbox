# TW API sandbox

Random quick-n-dirty scripts for experimenting with the TransferWise API

## Instructions

1. Download the dependencies
```
pip3 install -r requirements.txt
```

2. Generate a personal token in your [settings page](https://transferwise.com/user/settings) on the TransferWise site

3. Edit the file "\_auth.py" and replace the X's with your personal token in this file
```
API_TOKEN='123456-1234-1234-123456'
```

4. Run the script
```
python3 ./tw-get-statement.py EUR
EUR activity since 2019-10-25 11:45:49
+------------+--------+------------------------------------------------------------------------+-----------------+
|    Date    | Amount | Description                                                            | Running Balance |
+------------+--------+------------------------------------------------------------------------+-----------------+
| 21-11-2019 | -48.00 | Card transaction of 48.00 EUR issued by MyCo Ltd.                      |      161.96     |
| 21-11-2019 | -3.90  | Card transaction of 3.90 EUR issued by Gumps Shrimp                    |      209.96     |
| 20-11-2019 | -5.45  | Card transaction of 5.45 EUR issued by Fly Cafe, JFK Airport           |      213.86     |
| 19-11-2019 | 200.00 | Topped up balance                                                      |      219.31     |
+------------+--------+------------------------------------------------------------------------+-----------------+
```

