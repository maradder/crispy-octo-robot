from flask import Blueprint



world_blueprint = Blueprint('world', __name__, url_prefix='/world')


@world_blueprint.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"