# TW API sandbox

Random quick-n-dirty scripts for experimenting with the TransferWise API

## Instructions

1. Download the dependencies
```
pip3 install -r requirements.txt
```

2. Generate a personal token in your [settings page](https://transferwise.com/user/settings) on the TransferWise site

3. Edit the script and add your personal token near the top of the script
```
API_TOKEN='XXXXX-XXXX-XXXX-XXXX-XXXXXXXX'
```

4. Run the script
```
python3 ./tw-get-statement.py EUR
```

