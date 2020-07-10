from api import app, jsonify

@app.route("/")
def getProduct(): 
    return jsonify({'data': "Hello from get!"})

@app.route("/")
def createProduct(): 
    return jsonify({'data': "Hello from create!"})
