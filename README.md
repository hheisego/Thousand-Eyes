# Thousand-Eyes

This script purpose is integrate a Thousand Eyes alert(s) to Slack (instant messaging) services.
Optional added Webex Messaging Integration

## Requirements

* Thousand Eyes account or trial for testing purposes [Thousand Eyes signup!](https://www.thousandeyes.com/signup)
* Python 3.6 or above
* Public IP and open port for the TE, Webhook
* Slack account or free instance 
* Webex Account (Optional)

## Installation

- Create a Thousand Eyes _test_ with an alert and a rule that send a notification to your webhook

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries.

```bash
pip install requests random flask
```

* Optional <pip install webexteamssdk> (for Webex Messaging)
  
```python
import requests
import random
import json
from flask import Flask, request, jsonify
#from webexteamssdk import WebexTeamsAPI, ApiWarning # Optional
```
  
## Usage
  
  Create an Slack Application > [Webhook](https://api.slack.com/messaging/webhooks)
  Get Thousand Eyes [API Authorization](https://developer.thousandeyes.com/v6/#/authentication)
  
  Fill the secrets.json file with your own Thousand Eyes information, Slack Information Optional (Webex) and place this secrets file in the python file root folder.
  
  ```json
{
  "webex_bot_token": "NNNNWWWWWXXXXXYYYYYYZZZZ",
  "slack_webhook": "https://hooks.slack.com/services/NNNNWWWWWXXXXXYYYYYYZZZZ",
  "thousand_baerer": "NNNNWWWWWXXXXXYYYYYYZZZZ",
  "webex_room_id":  "NNNNWWWWWXXXXXYYYYYYZZZZ",
  "thousand_user": "user@domain:"
} 
  ```
 
## Comprobation

Create a Test Web-HTTP Alert pointing your Server Webhook in advanced settings configure this Test to send "GET" requests.
the script is listening "GET" requests and randomly responding with HTTP status codes:

```python
http_codes = [200, 201, 202, 206, 401, 402, 403, 404, 408, 500, 503]
.
.
...

    if request.method == 'GET':

        code = random.choice(http_codes)

        return jsonify({'status': 'Not Allowed Method'}), code

    return jsonify({'status': 'Listening'}), 200
```
  
