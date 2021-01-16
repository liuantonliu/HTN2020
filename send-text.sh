export MESSAGES_API_URL=https://api.nexmo.com/v0.1/messages
export JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MTA4MTI3MjIsImV4cCI6MTYxMDgzNDMyMiwianRpIjoienBhNXFJMm9Kczk1IiwiYXBwbGljYXRpb25faWQiOiIyZjA3NmY2Ni05ZmYwLTRhMjMtOWRhNi01Nzg2YTBhYjQwYzYifQ.Q0cW8ajLp1gbZxmBkcJj2qOvWX5EH0Yd1EfZGZD8Seys7CKE6aitTzL_En1hIzZ6bBIOQIY98tR7YoTAbN7_6J0AyKZMM3j-tzvxh1jwRn4vzEz-F0QLGBRpJ1A-Kgen0ot0yg2uxIn4ichvTS2anXs99EvemXw6RGdCZS48p43_U5m0NFTtKZC7PICV7tHgtuGRhU-a7mlsvwwudZF3GVOnGey-HRC4cgnNjH8403-2m2yoDFlSPd1rtfx9_hlXSPtlvYcUYC0Ox7A69RUui6_FWmC9syiXNX9cPnY8DNNBsPMHJhCeSUkQzyNbD-qWUpVBaiBj5cug1isnsUwjOA
export FB_SENDER_ID=103728078374712
export FB_RECIPIENT_ID=5279478152077378
curl -X POST $MESSAGES_API_URL \
  -H 'Authorization: Bearer '$JWT\
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d $'{
    "from": { "type": "messenger", "id": "'$FB_SENDER_ID'" },
    "to": { "type": "messenger", "id": "'$FB_RECIPIENT_ID'" },
    "message": {
      "content": {
        "type": "text",
        "text": "This is a Facebook Messenger Message sent from the Messages API"
      }
    }
  }'
