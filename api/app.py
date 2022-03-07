from flask import Flask, Response, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r'*': {'origins': '*'}})

#@app.route('/', defaults={'path': ''})
@app.route('/api/get_price', methods=["GET"])
def api():
    response_object = {"price": "1000"}
    response = Response(data=jsonify(response_object))
    return response
    #if request.method == 'GET':
        #response_object = {"price": "1000"}
        #return jsonify(response_object)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
