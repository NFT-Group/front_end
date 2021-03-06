from flask import Flask, Response, jsonify, request
from flask_cors import CORS
# from random import randint
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, db
import json
#from public.node_graph_data.helper_functions import find_price_predictor_from_tokenid


apeAddress = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'
cryptoPunkAddress = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'
doodlesAddress = '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e'
coolCatsAddress = '0x1A92f7381B9F03921564a437210bB9396471050C'
cloneXAddress = '0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B'
crypToadzAddress = '0x1CB1A5e65610AEFF2551A50f76a87a7d3fB649C6'
boredApeKennelAddress = '0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623'
pudgyPenguinAddress = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'

firebase_key = {
  "type": "service_account",
  "project_id": "allcollections-6e66c",
  "private_key_id": "903f6873f9f77f0c779a1f3de218f84d641c3e17",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDI0SIZAxQhL/D6\naFtiSvXB+h9fjeM5LydC003CFHlmPlIc8SEy0ialBvHjzzM/LDRwRUopI5LdO60G\n4xJ7iPrdTl5JoB85JHe++VXFuj4aUMPUIGO4xhLXWPfO8dr6We9WJ4ebGcO7HL9N\nlu0JhCFLERC21MNGidnnr/VM0La0PyuxhtDtdrKjjsyVzvmIhuSFR34gW+1F1O/a\noCR7iCH7YaSxxFODkLlllpJ6KrCkbYzFEH04j4r4aNV/ZSweYwZoM+PjgnfoYp1u\nOgXUi2N/Y8Ynx6CWNiW/51RwG+t5FqMKhOFHtaFVk0IKvg4FVWiL/QDqtiPY2Tc0\nJe5R05KNAgMBAAECggEAJHAKC1bLKsBrrcwMtNecIx/S3IA+2AvtyErWA566bmpl\ndNnt565JE82gS3E3v8EyHKL981wAlIL1ANhn7KFsv4YuRpa2w6QR1EWioheKmDTK\na62a2paaKZf7kwHAdYenDU9r5CE3KjbroVT+2qiub9P/X+VYL27o6oi7bj46wJaZ\nekCeYvOqQ8tlnzcorRYzG8UV6fe1kyz0PHgH6q8yR5/OUtAhxm9hdIC+VKNvJah+\npyvMd+9mN1uTtnxkmPxR9Sv3GJJ4wOLsn2Wgvuydq453dGRaN+u6DCnVipOTPUvt\n6MxiwXPur6FgnpY5QDiMNHMJeMCH+NKJq7plHPqg4QKBgQDk7Hk7LbUwF845OeTs\nSZUAqhj2Rh91Q70/fQ5aiS9HV39na8ZLNT7VjA5sT3uEm7SJ7A6CVQjXkT2EiOcp\nRk+4NKhktaesnZXpVnW2bTNJOd2K0wnvcagn6RccYjBDH+SrQoFL27Zv3+/GePFb\ncdf73cobSUme1iW6MIjEmvUr3QKBgQDgkZ7ilLWndN1ROQAnDXnr0nrzeD+6txEf\n8lq5BWLaxfBtaw2++CwcXPo3+9KqXnny71gUBIVJlmJv6HFk1499qPMNJ8WEd9qW\nvkfHSrnF5lMdAwvj1da5ergdLbnCfHRSzravP4bZSlKsCmGWrVPuUnD8QtGyPnZs\nouine8eucQKBgF8UqLWfomW7PXgfR6msVirUe1GuhlpaLDw2YMPRvsVO3ifCZ7XN\nA7AGX+c0jATj9vRiCxSu5OFD/d0ST5ChF3NWy6oomN/lA+LKelGuwWJkmlOSm8nL\n1x/cfDDZx1nZ4UwQb0tmkjudMyWoDfcBLcf6snrq0Z0bLMhMaEHganwxAoGAd/OQ\niLqiJSY5KS9nM3TxUNOGtRHgCJ3MWeIcL4P+/5iHCgsKtpzdAvFu/gRWzIXWYbsS\nsu6PO3VGczwXhaPWk2pxGO/Lgyx559cPhBYYEOssLez4puQL49r3CS7pcEcF401j\nK0ylfN9ENXz+D3vZvwzuKPCQDcNrgi+qUfu99yECgYEApEwuUUkvZnqRmUqJqlrI\nUO6SfjgluVZyqQku+44sWTj8YjgpX//wvEhJpNzSkqYMjDDYtCuhfHJoY+WgVvHt\nUCVrxZmXZ7b/tNVT+0SjMGFsZIKLfuyVyqrXeFSHtLMMxcepobF44kxzSGLvdn1i\ndL2GMhkNW5gSwstAuetsf+E=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ofrcq@allcollections-6e66c.iam.gserviceaccount.com",
  "client_id": "111391958965295617135",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ofrcq%40allcollections-6e66c.iam.gserviceaccount.com"
}

app = Flask(__name__)

CORS(app)

ml_app = None
transactions_app = None

@app.route('/api/get_transactions', methods=["POST"])
def get_transactions():
    cred = credentials.Certificate(firebase_key)
    try:
        firebase_admin.delete_app(ml_app)
    except:
        a = cred # dummy operation
    try:
        transactions_app = firebase_admin.initialize_app(cred, { 'databaseURL': "https://allcollections-6e66c-default-rtdb.europe-west1.firebasedatabase.app/" } )
    except:
        a = cred # dummy operation
    ref = db.reference('/')
    request_data = json.loads(request.data)
    timeframe = request_data['timeframe']
    data_type = request_data['data_type']
    if (timeframe == 'year'):
        start_time = time.time() - 31556952
    elif (timeframe == 'month'):
        start_time = time.time() - 2419200
    elif (timeframe == 'week'):
        start_time = time.time() - 604800
    elif (timeframe == 'day'):
        start_time = time.time() - 86400
        
    start_time = datetime.utcfromtimestamp(int(start_time)).strftime('%Y-%m-%d')
    transaction_list = ref.order_by_child('timestamp').start_at(start_time).get()
    transaction_keys = transaction_list.keys()
    transaction_data = [0, 0, 0, 0, 0, 0, 0, 0]
    collection_names = ['Bored Ape Yacht Club', 'CryptoPunks', 'Bored Ape Kennel Club', 'Cool Cats', 'cloneX', 'CrypToadz', 'Doodles', 'Pudgy Penguins']
    for key in transaction_keys:
        if transaction_list[key]['contracthash'] == apeAddress:
            if (data_type == 'volume'):
                transaction_data[0] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[0] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == cryptoPunkAddress:
            if (data_type == 'volume'):
                transaction_data[1] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[1] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == boredApeKennelAddress:
            if (data_type == 'volume'):
                transaction_data[2] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[2] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == coolCatsAddress:
            if (data_type == 'volume'):
                transaction_data[3] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[3] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == cloneXAddress:
            if (data_type == 'volume'):
                transaction_data[4] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[4] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == crypToadzAddress:
            if (data_type == 'volume'):
                transaction_data[5] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[5] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == doodlesAddress:
            if (data_type == 'volume'):
                transaction_data[6] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[6] += transaction_list[key]['ethprice']
        elif transaction_list[key]['contracthash'] == pudgyPenguinAddress:
            if (data_type == 'volume'):
                transaction_data[7] += 1
            elif (data_type == 'cumulative_value'):
                transaction_data[7] += transaction_list[key]['ethprice']
    
    response_json_array = []

    for i in range(8):
        response_json_array.append({'name': collection_names[i], 'size': transaction_data[i]})

    firebase_admin.delete_app(transactions_app) # there will DEFINITELY be a better way of doing this!!

    return jsonify(response_json_array)
