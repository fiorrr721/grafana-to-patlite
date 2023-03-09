from typing import Dict

from flask import Flask, request
import requests

PATLITES:Dict[str, str] = {
    "NHB" : "192.168.10.188",
    "LA6" : "192.168.10.189"
}

app = Flask(__name__)

@app.route('/<id>/api/control', methods=["GET", "POST"])
def control(id):
    #requestbody = request.json
    controlargs:Dict[str, str] = request.args
    
    #target_host = PATLITES[id]
    target_control_param = construct_param(controlargs)

    #print(target_control_param)
    #print(target_host)

    to_url = f"http://{id}/api/control?{target_control_param}"
    #print(to_url)
    requests.get(to_url)
    return "OK"


def construct_param(dict:Dict[str, str]) -> str:
    params = []
    for k, v in dict.items():
        params.append(f"{k}={v}")
    return "&".join(params)


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5050)
