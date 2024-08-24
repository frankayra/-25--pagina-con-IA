from flask import Flask
from api.auth import auth_bp
from api.cart import cart_bp
from api.orders import orders_bp
from api.products import products_bp
from database import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Registrar los Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(products_bp)

# Inicializar la base de datos
init_db()

@app.route('/')
def index():
    return 'Welcome to the E-commerce API'

if __name__ == '__main__':
    app.run(debug=True)
