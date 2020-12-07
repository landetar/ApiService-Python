from flask import Flask, request, jsonify, make_response

class LoginUser:
    def __init__(self):
        pass

    def get_message(self, ToEmail):
        return 'Hello ' + ToEmail + ' your message will be send.'
