from flask import Flask, Response, jsonify
from random import randint

app = Flask(__name__)

#@app.route('/', defaults={'path': ''})
@app.route('/api/get_price', methods=["GET"])
def api():
    price = randint(1000000, 10000000)
    response_string = "That NFT would cost " + str(price) + " pounds!"
    response_object = {"price": response_string}
    return jsonify(response_object)
    #if request.method == 'GET':
        #response_object = {"price": "1000"}
        #return jsonify(response_object)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
