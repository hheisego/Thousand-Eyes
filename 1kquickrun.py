
alarm = {'eventId': '439026526-118039164', 'alert': {'severity': 'Major', 'dateStartZoned': '2022-04-25 17:18:00 CDT', 'apiLinks': [{'rel': 'related', 'href': 'https://api.thousandeyes.com/v4/tests/2834877'}, {'rel': 'data', 'href': 'https://api.thousandeyes.com/v4/web/http-server/2834877'}], 'testLabels': [], 'active': 1, 'ruleExpression': 'Response Code is any error (â‰¥ 400 or no response)', 'type': 'HTTP Server', 'ruleAid': 1021286, 'agents': [{'dateStart': '2022-04-25 17:18:00', 'active': 1, 'metricsAtStart': 'Response Code: 402', 'metricsAtEnd': '', 'permalink': 'https://app.thousandeyes.com/alerts/list/?__a=1021286&alertId=118039164&agentId=1120', 'agentId': 1120, 'agentName': 'New York, NY (Cogent)'}, {'dateStart': '2022-04-25 17:18:00', 'active': 1, 'metricsAtStart': 'Response Code: 401', 'metricsAtEnd': '', 'permalink': 'https://app.thousandeyes.com/alerts/list/?__a=1021286&alertId=118039164&agentId=59220', 'agentId': 59220, 'agentName': 'Seattle, WA (Verizon)'}, {'dateStart': '2022-04-25 17:18:00', 'active': 1, 'metricsAtStart': 'Response Code: 404', 'metricsAtEnd': '', 'permalink': 'https://app.thousandeyes.com/alerts/list/?__a=1021286&alertId=118039164&agentId=63069', 'agentId': 63069, 'agentName': 'Dallas, TX (AT&T)'}], 'testTargetsDescription': ['http://live-demo22.online:5012/'], 'violationCount': 3, 'dateStart': '2022-04-25 17:18:00', 'ruleName': 'webhook-bots', 'testId': 2834877, 'alertId': 118039164, 'ruleId': 4599353, 'permalink': 'https://app.thousandeyes.com/alerts/list/?__a=1021286&alertId=118039164', 'testName': 'DSM-Server'}, 'eventType': 'ALERT_NOTIFICATION_TRIGGER'}

print(alarm['alert'].get('testName'))

output_alerts = '\nTest > Rule: ' + alarm['alert'].get('testName') + ' > ' +  alarm['alert'].get('ruleName')
for i in alarm['alert'].get('agents'):

    output_alerts += "\nResponse Code: " + str(i.get('metricsAtStart'))
    output_alerts += "\nAgent: " + str(i.get('agentName'))

print(output_alerts)