from flask import Flask, jsonify
from flaskr.blueprints import home, auth, products
from flaskr.models.Base import db

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
application.config['SECRET_KEY'] = 'abc123..'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

application.register_blueprint(home.bp)
application.add_url_rule('/', endpoint='index')
application.register_blueprint(auth.bp)
application.register_blueprint(products.bp)

db.init_app(application)

with application.app_context():
    db.create_all()

if __name__ == '__main__':
    application.debug = True
    application.run()