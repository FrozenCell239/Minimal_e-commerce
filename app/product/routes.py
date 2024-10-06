from app.extensions import db
from app.models.product import Product
from app.product import product_bp
from flask import render_template, redirect, url_for, request

@product_bp.route('/', methods = ['GET', 'POST'])
def index():
    products = Product.query.all()
    return render_template('product/index.html.jinja', products = products)

@product_bp.route('/new', methods = ['GET', 'POST'])
def create():
    print("OK 1")
    if request.method == 'POST' :
        print("OK 2")
        product = Product(
            name = request.form['product_name'],
            description = request.form['product_description'],
            price = request.form['product_price'],
            stock = request.form['product_stock']
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('product.index'))
    return render_template('product/new.html.jinja')

@product_bp.route('/<int:id>', methods = ['GET', 'POST'])
def read(id):
    product = Product.query.get_or_404(id)
    return render_template('product/read.html.jinja', product = product)

@product_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST' :
        product.name = request.form['product_name']
        product.description = request.form['product_description']
        product.price = request.form['product_price']
        db.session.commit()
        return redirect(url_for('product.index'))
    return render_template('product/edit.html.jinja', product = product)

@product_bp.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product.index'))