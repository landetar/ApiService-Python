from flask import Flask, request, jsonify, make_response

secretKey='Th1s1ss3cr3t'

class LoginUser:
    def __init__(self):
        pass

    def get_message(self, current_user):
        data = current_user.get_json()
        return jsonify({'message' : 'Hello ' + data['to'] + ' your message will be send'})
