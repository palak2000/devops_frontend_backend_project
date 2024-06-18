from flask import Flask, Blueprint, render_template, redirect, url_for
product_bp = Blueprint('product', __name__)

@product_bp.route('/')
def product_home():
    return render_template('product_details.html')

@product_bp.route('/products/<product_id>')
def product_details(product_id):
    product = {
        'product_id': product_id,
        'product_name': f'Product {product_id}',
        'price': 100.0 * int(product_id),  # Dummy calculation for different prices
        'description': f'Description of Product {product_id}'
    }
    return render_template('product_details.html', **product)

app = Flask(__name__)
app.register_blueprint(product_bp)

@app.route('/')
def home():
    return redirect(url_for('product.product_home'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

