# curl -H "Authorization: Bearer secret-token-1" http://127.0.0.1:7001/
# 19090070 - Fikriyah Khairunnisa
# 19090097 - Ika Bella Fitriani Putri
from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "secret-token-1": "Fikriyah",
    "secret-token-2": "Bella"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug = True, port=7001)
