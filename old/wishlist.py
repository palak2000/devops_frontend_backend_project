from flask import Blueprint, render_template, redirect, url_for

wishlist_bp = Blueprint('wishlist', __name__)

wishlist_items = []

@wishlist_bp.route('/wishlist')
def view_wishlist():
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@wishlist_bp.route('/wishlist/add/<product_id>')
def add_to_wishlist(product_id):
    wishlist_items.append(product_id)
    return redirect(url_for('product.product_details', product_id=product_id))

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(wishlist_bp)
    app.run(debug=True, host='0.0.0.0', port=5002)

