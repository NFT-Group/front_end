from flask import Flask, Response, jsonify, request
from random import randint
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, db
import json
import pickle

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

cred_push_key = {
  "type": "service_account",
  "project_id": "ml-prepped-database",
  "private_key_id": "b94db5e77d786b2608f10636b3baf757070974d6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDDtf8ceauQXcM9\nvOFP4mUUbuOTYk5twoU/LhdbeE8Gs6F+SrB+YA7WmurJTp/GwQdY7ThV7YKYtkSx\nsaFmYDjUHeJGgnq4QJyvSyWVf9kW8ZSMhWmt0kOcgeSLAKbqI6UOyIUsN/5rSe5K\ngxVeDKQCLW7IIzVZEDI+xkVeAYmiXuHsx+qqQ2lO0ki5bGtxyAvnJQ6dBS7hhYWf\nx9jzOPYB1YBV6wi55uhjOaj7Z+WcVz2ME2ybjvmMwX2oE0FyRE7H+s1RvzAltYQN\nCS95aX4YxWr1Fe/bMmzAlKkT9T+ccDu57Ix1dUl41Am1uoa1DjhAUls6UFqC3iX2\npPaRnWcvAgMBAAECggEAFG77kEMJzRxlBpyiX59RE2WSgDBa5O3S0KpkyOmSQq5d\nlZyBuegYlIJ/Mf5yAyPjOv8lix8tq/kXyf+0TMaOGGN4XQlBe9xPH6Q2a9n51gHq\nExPY2UujQIN1U6gBRV/sW1NHSDseZqBE72WpRPUH6KxKrT2z07UzsccstehuMNQN\nZ2aAR+rp9JcmGfUbHQ08usQF8lyRuhAkhomHY9OR5k0GWLzBrxqJHqHA/+E4EDH4\nLwFdL8zOtZmATbZHXqX55Uj8zGLws+2I/ksG3l8yZHeuitniqvpmKvhYc2ER2KLx\nAZ8ejevcWTMRVGHkX9XUxVG8NUWTH09vJ6W3jbgabQKBgQDuq0CSCA31aEbSXguf\nFJL63oyqRX5FGIz1wbzWyAOUndhpc1TupOQxnt1RQwLqwqb4Oy0C19rhSSF6h4BI\nHpNrnX6z65rhFGp0APHdt7kGZ4NApx7iiNkM/SGSCGPdaxYylZ3Rb1hE3Omit6VU\nEbm3NkoZVhjjsGWtKtaaSWugzQKBgQDR7CyJnE8V5lD/OrCd5BZqIhBxbBD299+R\nDs8hnrktw+Gtvn9WwLql0AUIstSV7m7W7eJYvD1h3AUbO2o/H7+bmneIHARt8DrP\nQQLnholcX+aPAEKuokesEpjEoleqTI8epu5dwE2uuYgF7P7QqbhWWFaBkYqjQTFj\nVio9Zlf36wKBgAvok5I1wKyMBWydsKrBVgwaap5cVU6RSQdCIW/+Dt+teIzaalR1\n+cTYDmbtlwmrqLUeDsLjjlJLWdZJSIdQrz5hX18O1G2CnUUofuj3L843//6L2Cip\nd1sEjlZBAOqdW0Au4u7+RUM6WpX538/wCnovxUa6WweRV6FqT8bm/u3JAoGAFA4B\nD0B8mbYAJPIBb4Qb1BXfBkbxs/ZoSF5m0WptfH7LL6MUXUBaVH70DCmxf4Vg122w\ngxOwtYmkfz6E3vT0hDQUmU876RjbNXObiGzk8ItE5oJ63F4qhLjeGWL9Bwr7XU1L\nVm+JvFiDMzW5/ktIjg8wbH5wBTq0Mi5IKMd/PfMCgYEAqq6OAWU2CcNu2MJdPaON\nEraEdyO8UmTeRNcAsI/DVfJkOgDWs/mON33Cmtnmc4HHSf6YsjHBy+g8XCkWBPdb\n4RqguTSBbMdbpSjinnkocJF5UcMMjKWUfOBdymWMrQao14tAxtuSvqtSY1fvUCB+\n1Ohu36IjTNi8LW1kGi//zII=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-u7cos@ml-prepped-database.iam.gserviceaccount.com",
  "client_id": "110669828910428993200",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-u7cos%40ml-prepped-database.iam.gserviceaccount.com"
}

app = Flask(__name__)

# CREATE LINK FOR 'FULL DATABASE'

def find_price_predictor_from_tokenid(request):
    # process request
    collection_name = request['collection']
    tokenID = request['tokenid']

    # find model
    filename = collection_name + "_model.txt"
    loaded_model = pickle.load(open(filename, 'rb'))

    # find input
    nft_string = collection_name+tokenid
    ref = db.reference(nft_string)
    data_for_input = ref.get()

    # format input 
    data_for_input_json = pd.DataFrame([data_for_input])
    data_for_input_json = data_for_input_json.drop(['NameOfCollection', 'ethprice'], axis=1)
    data_for_input_json['timestamp'] = 0

    predicted_price = loaded_model.predict(data_for_input_json)
    return predicted_price


        

#@app.route('/', defaults={'path': ''})
@app.route('/api/get_price', methods=["POST"])
def api():
    #cred_push_key = str(pathlib.Path(__file__).parent.resolve()) + '/database_store_keys/key_for_ML-prepped-database.json'
    cred_push = firebase_admin.credentials.Certificate(cred_push_key)
    try:
        ml_app = firebase_admin.initialize_app(cred_push, { 'databaseURL':'https://ml-prepped-database-default-rtdb.europe-west1.firebasedatabase.app/' }, 'ml_app' )
    except:
        a = cred_push # dummy operation
    collection = json.loads(str(request.data)[2:-1])
    price = find_price_predictor_from_tokenid(collection) #randint(100, 10000000)
    response_json = {"price" : "That " + str(collection)[2:-1] + " would cost £" + str(price) + "! Wow!"}
    firebase_admin.delete_app(ml_app) # there will DEFINITELY be a better way of doing this!!
    return jsonify(response_json)
    #if request.method == 'GET':
        #response_object = {"price": "1000"}
        #return jsonify(response_object)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

def machine_learning(a):
    return 

@app.route('/api/get_weeks_transactions', methods=["GET"])
def get_weeks_transactions():
    cred = credentials.Certificate(firebase_key)
    try:
        transactions_app = firebase_admin.initialize_app(cred, { 'databaseURL': "https://allcollections-6e66c-default-rtdb.europe-west1.firebasedatabase.app/" } )
    except:
        a = cred # dummy operation
    ref = db.reference('/')
    one_week_ago = time.time() - 604800 #number of seconds in a week
    one_week_ago = datetime.utcfromtimestamp(int(one_week_ago)).strftime('%Y-%m-%d')
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

    firebase_admin.delete_app(transactions_app) # there will DEFINITELY be a better way of doing this!!

    return jsonify(response_json_array)
