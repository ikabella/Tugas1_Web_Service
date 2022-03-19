#curl -u john:hello http://127.0.0.1:7002/
#Fikriyah Khairunnisa - 19090070
#Ika Bella Fitriani Putri - 19090097

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "19090070": generate_password_hash("123"),
    "19090097": generate_password_hash("123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/api/v2/users/info')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug = True, port=4000)
