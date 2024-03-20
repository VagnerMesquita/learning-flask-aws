from flask import Flask
import requests

app = Flask(__name__)

@app.route("/pudim")
def api():
    headers = {"X-Parse-Application-Id":"lx03BLJ08F9S9la2EcWBKfdlZ1aAFrSPwBVweGlW",
            "X-Parse-REST-API-Key": "CygcDai6A2NYfWvS4C4JWyV0G4ur6grCqlLtkNki"}


    r = requests.post(f'https://parseapi.back4app.com/functions/get-norma', headers=headers, data= {"normaId": "qyfDq57psG"} )
    channelId = r.json()['result'][0]['channelId']
    channelName = r.json()['result'][0]['channelName']

    print(channelName)
    return {"message": channelName}