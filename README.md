# TW API sandbox

Random quick-n-dirty scripts for experimenting with the TransferWise API

## Instructions

1. Download the dependencies
```
pip3 install -r requirements.txt
```

2. Generate a personal token in your [settings page](https://transferwise.com/user/settings) on the TransferWise site

3. Edit the file "i\_auth.py" and replace the X's with your personal token in this file
```
API_TOKEN='123456-1234-1234-123456'
```

4. Run the script
```
python3 ./tw-get-statement.py EUR
```

