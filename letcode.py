from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
url = "https://leetcode.com/api/problems/all/"

headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST", "GET"])
def getrepond():
    cookies = {}
    if request.method == "POST":
        req = request.json["cookie"]
        key, value = req.split("=",1)
        cookies[key] = value
    else:
        cookies = {"__stripe_mid": "6bb71d6f-fa5f-43ec-bf36-d6e66c2692265ecb8b; csrftoken=fTUaLNXUXehPYjeaADJWPwxWz6LHBcfu98tCr1p0K8zADm5pp0DFTAiEDmRJMmRt; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDMyNzEwMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmU0NDc4ZGU4ZWYwYWQyMjI3NzE1NDgxMjcyN2UxOGNhMzNjNjc2OCIsImlkIjo0MzI3MTAxLCJlbWFpbCI6ImhhcnNobTE3MTcyNjEyQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiTWlIYXJzaCIsInVzZXJfc2x1ZyI6Ik1pSGFyc2giLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY0MTUyNzU0Ni5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NTIyODkzNTgsImlwIjoiMTExLjIyMy4yNi4xNzYiLCJpZGVudGl0eSI6IjMzYWZhOTlhODk3MWJjZDEzMDY3ODhjZjViNTUzZjZkIiwic2Vzc2lvbl9pZCI6MjEzNDI3NTYsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.gaY7yQm5_R0Om4Qr0FExfWKUMj9w1iOoWh6a9_LzmbA; NEW_PROBLEMLIST_PAGE=1"}

    resp = requests.get(url, headers=headers, cookies=cookies)
    question_list = json.loads(resp.content.decode('utf-8'))
    solved = {}
    for question in question_list['stat_status_pairs']:

        if question["status"] == "ac":

            solved[question['stat']["frontend_question_id"]] = "ac"

    return jsonify({"solved": solved})


app.run(port=5000)
