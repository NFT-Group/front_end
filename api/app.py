from flask import Flask, Response, jsonify, request
from random import randint

app = Flask(__name__)

# CREATE LINK FOR 'FULL DATABASE'

cred_push_key = str(pathlib.Path(__file__).parent.resolve()) + '/database_store_keys/key_for_ML-prepped-database.json'
cred_push = firebase_admin.credentials.Certificate(cred_push_key)
default_app = firebase_admin.initialize_app(cred_push, {
    'databaseURL':'https://ml-prepped-database-default-rtdb.europe-west1.firebasedatabase.app/'
    })


def find_price_predictor_from_tokenid(collection_name, tokenid):
    # find model
    filename = collection_name + "_model.pkl"
    loaded_model = pickle.load(open(filename, 'rb'))

    # find input
    nft_string = collection_name+tokenid
    ref = db.reference(nft_string)
    data_for_input = ref.get()

    # format input 
    data_for_input_json = pd.DataFrame([data_for_input])
    data_for_input_json = data_for_input_json.drop(['NameOfCollection', 'ethprice', axis=1])
    data_for_input_json['timestamp'] = 0

    predicted_price = loaded_model.predict(data_for_input_json)
    return predicted_price


        

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

def machine_learning(a):
    return a+1