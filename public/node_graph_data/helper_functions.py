import pickle
import firebase
from firebase_admin import credentials, firestore, db
import pandas as pd


def find_price_predictor_from_tokenid(request):
    # process request
    collection_name = request['collection']
    tokenID = request['tokenid']

    # find model
    filename = "../node_graph_data/" + collection_name + "_model.pkl"

    loaded_model = pickle.load(open(filename, 'rb'))

    # find input
    nft_string = collection_name+tokenID
    ref = db.reference(nft_string)
    data_for_input = ref.get()

    # format input 
    data_for_input_json = pd.DataFrame([data_for_input])
    data_for_input_json = data_for_input_json.drop(['NameOfCollection', 'ethprice'], axis=1)
    data_for_input_json['timestamp'] = 0

    predicted_price = loaded_model.predict(data_for_input_json)

    predicted_price = 0

    return predicted_price

