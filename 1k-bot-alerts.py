import requests
import random
import json
from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI, ApiWarning


with open("secrets.json") as f:
    configs = json.loads(f.read())

def get_env_var(setting, configs=configs):

    try:
        val = configs[setting]
        if val == "True":
            val = True
        elif val == "False":
            val = False
        return val

    except KeyError:

        raise NotImplementedError("secrets.json is missing")

#Variables
http_codes = [200, 201, 202, 206, 401, 402, 403, 404, 408, 500, 503]

class ThousandEyesAlert:

    slack_webhook = get_env_var("slack_webhook")
    thousand_url = "https://" + get_env_var("thousand_user") + get_env_var("thousand_baerer") + "@api.thousandeyes.com/v6/"


    def get_tests(self):

        url = self.thousand_url + "tests.json"

        tests = requests.get(url).json()

        return tests


    def send_msg_slack(self, msg):

        msg = {"text": msg}

        send_msg_slack = requests.post(url=self.slack_webhook, json=msg)

        return send_msg_slack.status_code

    def send_msg_webex(self, msg):

        webex_room_id = get_env_var("webex_room_id")
        webex_bot.messages.create(roomId=webex_room_id, text=msg)

        return ApiWarning


#Object Instances
webex_bot = WebexTeamsAPI(access_token=get_env_var("webex_bot_token"))
eyes = ThousandEyesAlert()
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main_page():

    if request.method == 'POST':

        alarm = request.json
        output_alert = '\nTest > Rule: ' + alarm['alert'].get('testName') + ' > ' + alarm['alert'].get('ruleName')

        for i in alarm['alert'].get('agents'):

            output_alert += "\nResponse Code: " + str(i.get('metricsAtStart'))
            output_alert += "\nAgent: •" + str(i.get('agentName'))

            eyes.send_msg_slack(msg=output_alert)
            eyes.send_msg_webex(msg=output_alert)

        return jsonify({'status': 'Alert Received'}), 200

    if request.method == 'GET':

        code = random.choice(http_codes)

        return jsonify({'status': 'Not Allowed Method'}), code

    return jsonify({'status': 'Listening'}), 200


if __name__ == "__main__":
    # Do not keep debug=True in production
    app.run(host='0.0.0.0', port=5012, use_reloader=True, debug=True)  #, ssl_context='adhoc'

