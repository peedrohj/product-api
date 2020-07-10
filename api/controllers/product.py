from api import app, jsonify

@app.route("/")
def getProduct(): 
    """
        This route will recive an id and reutrn a product that have this id
    """

    return jsonify({'data': "Hello from get!"})

@app.route("/")
def createProduct(): 
    """
        This route will recive some products parameters and create this product
    """

    return jsonify({'data': "Hello from create!"})
