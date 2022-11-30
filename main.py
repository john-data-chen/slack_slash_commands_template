import os
import json
import requests
from flask import jsonify
import functions_framework
from slack.signature import SignatureVerifier

# [START functions_verify_webhook]
def verify_signature(request):
    request.get_data()  # Decodes received requests into request.data

    verifier = SignatureVerifier(os.environ['SLACK_SIGNING_SECRET'])

    if not verifier.is_valid_request(request.data, request.headers):
        raise ValueError('Invalid request/credentials.')
# [END functions_verify_webhook]

# [START functions_delist]
def make_delist_request(query):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': os.environ['AUTH_IN_HEADER']
    }
    json_data = json.dumps({
        'sku': query,
    })
    url = ''
    print(url)
    response = requests.post(url, headers=headers, data=json_data)
    if response.status_code == 200:
        result = 'done'
    else:
        result = 'fail'
    message = {
        'response_type': 'in_channel',
        'text': 'result: {}'.format(result)
    }
    return message
# [END functions_delist]

@functions_framework.http
def example(request):
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405

    verify_signature(request)
    response = make_delist_request(request.form['text'])
    return jsonify(response)