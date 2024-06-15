from flask import Blueprint, render_template

product_bp = Blueprint('product', __name__)

@product_bp.route('/products/<product_id>')
def product_details(product_id):
    # Dummy data for product details
    product = {
        'product_id': product_id,
        'product_name': 'Product Name',
        'price': 100.0,
        'description': 'Product Description'
    }
    return render_template('product.html', **product)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(product_bp)
    app.run(debug=True, host='0.0.0.0', port=5001)

