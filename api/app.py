from flask import Flask, Response, jsonify, request
from random import randint
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, db

apeAddress = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'
cryptoPunkAddress = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'
doodlesAddress = '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e'
coolCatsAddress = '0x1A92f7381B9F03921564a437210bB9396471050C'
cloneXAddress = '0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B'
crypToadzAddress = '0x1CB1A5e65610AEFF2551A50f76a87a7d3fB649C6'
boredApeKennelAddress = '0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623'
pudgyPenguinAddress = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'

app = Flask(__name__)

#@app.route('/', defaults={'path': ''})
@app.route('/api/get_price', methods=["POST"])
def api():
    collection = request.data
    price = machine_learning(10) #randint(100, 10000000)
    response_json = {"price" : "That " + str(collection)[2:-1] + " would cost £" + str(price) + "! Wow!"}
    return jsonify(response_json)
    #if request.method == 'GET':
        #response_object = {"price": "1000"}
        #return jsonify(response_object)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

#def machine_learning(a):
    #return a+1

@app.route('/api/get_weeks_transactions', methods=["GET"])
def get_weeks_transactions:
    cred = credentials.Certificate('../firebase_files/allCollections_key.json')
    firebase_admin.initialize_app(cred, { 'databaseURL': "https://allcollections-6e66c-default-rtdb.europe-west1.firebasedatabase.app/" } )
    ref = db.reference('/')
    one_week_ago = time.time() - 604800 #number of seconds in a week
    one_week_ago = datetime.utcfromtimestamp(int(current_time)).strftime('%Y-%m-%d')
    weeks_transactions = ref.order_by_child('timestamp').start_at(one_week_ago).get()
    transaction_keys = weeks_transactions.keys()
    total_transaction_counts = [0, 0, 0, 0, 0, 0, 0, 0]
    collection_names = ['Bored Ape Yacht Club', 'CryptoPunks', 'Bored Ape Kennel Club', 'Cool Cats', 'cloneX', 'CrypToadz', 'Doodles', 'Pudgy Penguins']
    for key in transaction_keys:
        if weeks_transactions[key]['contracthash'] == apeAddress:
            total_transaction_counts[0] += 1
        if weeks_transactions[key]['contracthash'] == cryptoPunkAddress:
            total_transaction_counts[1] += 1
        if weeks_transactions[key]['contracthash'] == boredApeKennelAddress:
            total_transaction_counts[2] += 1
        if weeks_transactions[key]['contracthash'] == coolCatsAddress:
            total_transaction_counts[3] += 1
        if weeks_transactions[key]['contracthash'] == cloneXAddress:
            total_transaction_counts[4] += 1
        if weeks_transactions[key]['contracthash'] == crypToadzAddress:
            total_transaction_counts[5] += 1
        if weeks_transactions[key]['contracthash'] == doodlesAddress:
            total_transaction_counts[6] += 1
        if weeks_transactions[key]['contracthash'] == pudgyPenguinAddress:
            total_transaction_counts[7] += 1
    
    response_json_array = []

    for i in range(8):
        response_json_array.append({'name': collection_names[i], 'size': total_transaction_counts[i]})

    return jsonify(response_json_array)
