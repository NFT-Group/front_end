from flask import Flask, Response, jsonify

app = Flask(__name__)

#@app.route('/', defaults={'path': ''})
@app.route('/api/get_price', methods=["GET"])
def api():
    response_object = {"price": "That NFT would cost a million billion pounds!"}
    return jsonify(response_object)
    #if request.method == 'GET':
        #response_object = {"price": "1000"}
        #return jsonify(response_object)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
