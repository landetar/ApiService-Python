from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
import json
from functools import wraps
from login import LoginUser

app = Flask(__name__)

with open('users.json') as file:
    users = json.load(file)

secretKey='Th1s1ss3cr3t'

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'X-Parse-REST-API-Key' in request.headers:
            token = request.headers['X-Parse-REST-API-Key']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, secretKey)
            current_user = [user for user in users['users'] if user['id'] == data['public_id']]
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator

@app.route('/DevOps/login', methods=['GET', 'POST'])
def login_user():

    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'DevOps Authentication': 'Basic realm: "auth required"'})

    for user in users['users']:
        if user['login'] == auth.username:
            if user['password'] == auth.password:
                token = jwt.encode({'public_id': user['id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, secretKey)
                return jsonify({'token' : token.decode('UTF-8')})

    return make_response('could not verify',  401, {'DevOps Authentication': 'Basic realm: "password incorrect"'})

@app.route('/DevOps/message', methods=['POST', 'GET'])
@token_required
def get_message(current_user):
    data = request.get_json()
    return jsonify({'message' : 'Hello ' + data['to'] + ' your message will be send'})

@app.route('/DevOps/ping')
def ping():
    return jsonify({"message": 'The conection was sucessfull'})

if __name__ == "__main__":
    app.run(debug=False, port=4000)

