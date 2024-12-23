from flask import Flask
from app.routes.world import world_blueprint


app = Flask(__name__)



app.register_blueprint(world_blueprint, url_prefix='/world')


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the little test"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello from app.py!"


if (__name__ == "__main__"):
    app.run(debug=True)