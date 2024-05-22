from flask import Blueprint, render_template, redirect, url_for

cart_bp = Blueprint('cart', __name__)

cart_items = []

@cart_bp.route('/cart')
def view_cart():
    return render_template('cart.html', cart_items=cart_items)

@cart_bp.route('/cart/add/<product_id>')
def add_to_cart(product_id):
    cart_items.append(product_id)
    return redirect(url_for('product.product_details', product_id=product_id))



