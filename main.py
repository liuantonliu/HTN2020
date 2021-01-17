# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging
from flask import Flask
from flask import request
from flask import jsonify
import requests
import asyncio 

url = "https://api.nexmo.com/v0.1/messages"

payload="{\r\n  \"to\": {\r\n    \"type\": \"messenger\",\r\n    \"id\": \"103728078374712\"\r\n  },\r\n  \"from\": {\r\n    \"type\": \"messenger\",\r\n    \"id\": \"10372878374712\"\r\n  },\r\n  \"message\": {\r\n    \"content\": {\r\n      \"type\": \"text\",\r\n      \"text\": \"Hello From Vonage!\"\r\n    }\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MTA4NDI2MDgsImV4cCI6MTYxMDkwMDIwOCwianRpIjoiaktIMHViZURDY0NJIiwiYXBwbGljYXRpb25faWQiOiI5NWE5ODM3Mi0yNjhmLTRkMTEtYTBlYS0xN2ZhNWZmZjkxYTIifQ.grOU0KnW5lGxomGD5oYWclPK_SgPuHdHZiIuh_RZCY6xmf4v1QR3SIMPkG6wu-hVc-r6-S7IuRM8zyuFWZD_OLzaF_w-PbeYyiesv5M5dn68Mx5-BsPmjazv8Y0ApqmLLOa4-RxYjxmmg1kT2GXWcJ-Dij-rptGb_FZcc5U7p0revDsvLReIVBGv2BuFTbMklWsM0cUeFytEBCPW8rfuaYqmG4uCg90ISOrP2Rm-YZtfGy5vRT1rlVcCtweqLx61W0X-Zf0vthYM-3ik76aW4Wcl5LyGV9M-KkBFjA0oYn1MXfgxaHaqS0MotyLAffQRd6BrGDoOjiwJVXYxzNh3_Q',
  'Content-Type': 'application/json'
}

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/messages', methods=['GET', 'POST'])
def receive_message(): 
    data = request.get_json()
    #print(data)
    message = data['message']['content']['text']
    page_id = data['to']['id']
    user_id = data['from']['id']

    #ML Model to generate response 
    response = "this"
    json_model = {
        "to": { 
            "type": "messenger",
            "id": str(user_id)
        },
        "from": { 
            "type": "messenger",
            "id": str(page_id)
        },
        "message": { 
            "content": { 
                "type": "text",
                "text": response
            }
        }
    }
    print(json_model)
    print(requests.post(url, headers=headers, json=json_model))

    #response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    return "Message sent successfully", 200


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
#a8c4c4dafd40839d3c3e3edb1505f42d4a8422a9