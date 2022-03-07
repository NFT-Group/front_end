from flask import Flask, Response
app = Flask(__name__)

#@app.route('/', defaults={'path': ''})
@app.route('/predictions', methods=["POST"])
def catch_all():
    return "hello from app.py!"
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
