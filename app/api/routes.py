from app.api import api_bp
from app.extensions import db
from app.models.product import Product
from flask import jsonify, request

@api_bp.route('/', methods = ['GET', 'POST'])
def index() :
    return jsonify({'message' : "Hello world !"})

@api_bp.route('/product/list', methods = ['GET', 'POST'])
def product_list() :
    try :
        result = []
        products = Product.query.all()
        for product in products :
            result.append({
                "id" : product.id,
                "name" : product.name,
                "description" : product.description,
                "price" : product.price,
                "stock" : product.stock,
            })
        return jsonify(result), 200

    except Exception as e :
        return jsonify({"Internal server error" : str(e)}), 500

@api_bp.route('/product/create', methods = ['POST'])
def product_create() :
    errors = []
    try :
        # Getting the product data from the request
        name = request.json.get('name')
        price = request.json.get('price')
        description = request.json.get('description')
        stock = request.json.get('stock')

        # Checking if the product already exists
        product = Product.query.filter_by(name = name).first()
        if product : errors.append("Product already exists !")

        # Checking if the product data is valid
        if not name : errors.append("Name is required !")
        if not description : errors.append("Description is required !")
        if not price :
            errors.append("Price is required !")
        else :
            if not isinstance(price, (int, float)) :
                errors.append("Price must be an integer or a float !")
            else :
                if price < 0 : errors.append("Price must be positive or null !")
        if not stock :
            errors.append("Stock is required !")
        else :
            if not isinstance(stock, int) :
                errors.append("Stock must be an integer !")
            else :
                if stock < 0 : errors.append("Stock must be positive or null !")

        # Checking if errors occurred
        if errors != [] : return jsonify({"errors" : errors}), 400
        
        # Creating the product
        product = Product(
            name = name,
            price = price,
            description = description,
            stock = stock
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({'message' : "Product created successfully !"}), 200

    except Exception as e :
        return jsonify({"Internal server error" : str(e)}), 500

@api_bp.route('/product/update/', methods = ['PUT'])
def product_update() :
    errors = []
    try :
        # Getting the product data from the request
        name = request.json.get('name')
        price = request.json.get('price')
        description = request.json.get('description')
        stock = request.json.get('stock')

        # Checking if the product exists
        product = Product.query.get(request.json.get('id'))
        if not product : return jsonify({'message' : "Product not found !"}), 404

        # Checking if the product data is valid
        if not name : errors.append("Name is required !")
        if not description : errors.append("Description is required !")
        if not price :
            errors.append("Price is required !")
        else :
            if not isinstance(price, (int, float)) :
                errors.append("Price must be an integer or a float !")
            else :
                if price < 0 : errors.append("Price must be positive or null !")
        if not stock :
            errors.append("Stock is required !")
        else :
            if not isinstance(stock, int) :
                errors.append("Stock must be an integer !")
            else :
                if stock < 0 : errors.append("Stock must be positive or null !")
        
        # Checking if errors occurred
        if errors != [] : return jsonify({"errors" : errors}), 400

        # Updating the product
        product.name = name
        product.price = price
        product.description = description
        product.stock = stock
        db.session.commit()
        return jsonify({'message' : "Product updated successfully !"}), 200

    except Exception as e :
        return jsonify({"Internal server error" : str(e)}), 500

@api_bp.route('/product/delete/', methods = ['DELETE'])
def product_delete() :
    try :
        # Checking if the product exists
        product = Product.query.get(request.json.get('id'))
        if not product : return jsonify({'message' : "Product not found !"}), 404

        # Deleting the product
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message' : "Product deleted successfully !"}), 200

    except Exception as e :
        return jsonify({"Internal server error" : str(e)}), 500