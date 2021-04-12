''' Our server file'''
# disabling some of the errors
# pylint: disable= E1101, C0413, R0903, W0603, W1508

import os
import operator  # for reordering the scores table
from flask import Flask, send_from_directory, json
from flask import request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from db_api import *
import datetime


load_dotenv(find_dotenv())  # This is to load your env variables from .env

APP = Flask(__name__, static_folder='./build/static')
# Point SQLAlchemy to your Heroku database
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)
# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues
import models

DB.create_all()

USER=''

@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    '''
    starting point
    '''
    return send_from_directory('./build', filename)


@APP.route('/login', methods=['POST'])
def login():
    '''login function obtains user info'''
    global USER
    user_info = request.json
    if user_info:
        print(user_info)
        USER = DBQuery(
            user_info['userInfo']['GoogleId'],
            user_info['userInfo']['Email'],
            user_info['userInfo']['FirstName'],
            user_info['userInfo']['LastName'])
            
        return jsonify(200)
    return jsonify(400)
    
@APP.route('/home', methods=['Get'])
def home():
    '''home function obtains user info'''
    global USER
<<<<<<< HEAD
    user_info = request.json
    print("in the function for home")
    print(request.method)
    print(user_info)
    # USER.addTransaction("Expense",123.00,
    #     datetime.datetime.strptime("05/31/2019", "%m/%d/%Y").date(),
    #     "Nike",
    #     "Sneakers")
    if request.method == 'GET':
        print("recieved request")
        print(user_info)
        print(USER.getTransactions())
        return USER.getTransactions()
    return jsonify(400)



=======
    transactions = USER.getTransactions()
    return (jsonify(transactions))
>>>>>>> 83d855bb3f45bc89361cfb08c1d2dac6b8bd40b9

if __name__ == "__main__":
    APP.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
