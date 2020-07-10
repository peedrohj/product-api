from api import app, jsonify, db, request
from api.models.product import Product


@app.route("/get/all_products", methods=['GET'])
def list_product():
    """
        This route will return all products
    """

    try:
        products = Product.query.all()
        product_list = [product.get_object() for product in products]

        return jsonify({"status": "success", "data": product_list})

    except Exception as error:
        return jsonify({"status": "error", "error": str(error)})


@app.route("/get/product/<id_>", methods=['GET'])
def get_product(id_):
    """
        This route will recive an id and return a product that have this id
    """

    try:
        product = Product.query.filter_by(id=id_).first()

        return jsonify({"status": "success", "data": product.get_object()})

    except Exception as error:
        return jsonify({"status": "error", "error": str(error)})


@app.route("/create/product", methods=['GET', 'POST'])
def create_product():
    """
        This route will recive a name and a description and save it in database
    """

    try:
        name = request.args.get("name")
        description = request.args.get("description")

        product = Product(name, description)

        db.session.add(product)
        db.session.commit()

        return jsonify({"status": "success", "data": "Create product with success"})

    except Exception as error:
        return jsonify({"status": "error", "error": str(error)})


@app.route("/delete/product/<id_>", methods=['GET', 'POST'])
def delete_product(id_):
    """
        This route will recive an id and delete a product by this id
    """

    try:
        product = Product.query.filter_by(id=id_).first()

        db.session.delete(product)
        db.session.commit()

        return jsonify({"status": "success", "data": "Delete product with success"})
    except Exception as error:
        return jsonify({"status": "error", "error": str(error)})
