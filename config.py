from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db
from database.models.cliente import Cliente


def config_all(app):
    config_routes(app)
    config_db()

def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/cliente')

def config_db():
    db.connect()
    db.create_tables([Cliente])