from flask import Flask, render_template, redirect, url_for
from product import product_bp
from wishlist import wishlist_bp
from cart import cart_bp

app = Flask(__name__)

# Register blueprint for the product microservice
app.register_blueprint(product_bp)
app.register_blueprint(wishlist_bp)
app.register_blueprint(cart_bp)

# Route for the root URL to display the product page
@app.route('/')
def index():
    # Redirect to the product page
    return redirect(url_for('product.product_details', product_id=1))

if __name__ == "__main__":
    app.run(debug=True)



