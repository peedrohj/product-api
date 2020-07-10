from api import app, jsonify, db
from api.models.product import Product


@app.route("/")
def list_product():
    """
        This route will recive an id and reutrn a product that have this id
    """

    try:
        products = Product.query.all()
        product_list = [product.get_object() for product in products]

        return jsonify({"status": "success", 'data': product_list})
    except Exception as error:
        return jsonify({"status": "error", 'error': str(error)})


@app.route("/get/product/<id_>")
def get_product(id_):
    """
        This route will recive an id and reutrn a product that have this id
    """
    try:
        product = Product.query.filter_by(id=id_).first()

        return jsonify({"status": "success", 'data': product.get_object()})
    except Exception as error:
        return jsonify({"status": "error", 'error': str(error)})


@app.route("/create")
def create_product():
    """
        This route will recive some products parameters and create this product
    """
    product = Product("Nome", "descricao")

    db.session.add(product)
    db.session.commit()

    return jsonify({"status": "success", 'data': 'Create product with success'})
