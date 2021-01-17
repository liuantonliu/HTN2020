import logging
from flask import Flask, request
import requests
import json


url = "https://api.nexmo.com/v0.1/messages"


headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MTA4NDI2MDgsImV4cCI6MTYxMDkwMDIwOCwianRpIjoiaktIMHViZURDY0NJIiwiYXBwbGljYXRpb25faWQiOiI5NWE5ODM3Mi0yNjhmLTRkMTEtYTBlYS0xN2ZhNWZmZjkxYTIifQ.grOU0KnW5lGxomGD5oYWclPK_SgPuHdHZiIuh_RZCY6xmf4v1QR3SIMPkG6wu-hVc-r6-S7IuRM8zyuFWZD_OLzaF_w-PbeYyiesv5M5dn68Mx5-BsPmjazv8Y0ApqmLLOa4-RxYjxmmg1kT2GXWcJ-Dij-rptGb_FZcc5U7p0revDsvLReIVBGv2BuFTbMklWsM0cUeFytEBCPW8rfuaYqmG4uCg90ISOrP2Rm-YZtfGy5vRT1rlVcCtweqLx61W0X-Zf0vthYM-3ik76aW4Wcl5LyGV9M-KkBFjA0oYn1MXfgxaHaqS0MotyLAffQRd6BrGDoOjiwJVXYxzNh3_Q',
  'Content-Type': 'application/json'
}


app = Flask(__name__)


@app.route('/')
def health_check():
    return 'HTN'


@app.route('/messages', methods=['GET', 'POST'])
def receive_message():
    data = request.get_json()
    print(f'Data received from Vonage: {json.dumps(data)}')
    message = data['message']['content']['text']
    page_id = data['to']['id']
    user_id = data['from']['id']

    #ML Model to generate response 
    response = "this"
    json_model = {
        "to": { 
            "type": "messenger",
            "id": user_id
        },
        "from": { 
            "type": "messenger",
            "id": page_id
        },
        "message": { 
            "content": { 
                "type": "text",
                "text": response
            }
        }
    }
    print(f'Sending data to Vonage API: {json.dumps(json_model)}')
    res = requests.post(url, headers=headers, json=json_model)
    if not res.ok:
        print('Error: ', res.json())
        return "Error", 500
    print(f"Response from Vonage API: {res.json()}")
    return "Message sent successfully", 200


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
