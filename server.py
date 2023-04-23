import os
from flask import (
    Flask, send_from_directory, redirect
)
from werkzeug.exceptions import NotFound
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'super-secret',
        SQLALCHEMY_DATABASE_URI='sqlite:///app.db',
    )
    app.config['DEBUG'] = True

    from db_models import User
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    import apis
    app.register_blueprint(apis.bp)

    @app.route('/')
    def index():
        return send_from_directory('client/build', 'index.html')



    @app.route("/<path:path>")
    def home(path):
        try:
            return send_from_directory('client/build', path)
        except NotFound:
            return redirect('/')

    return app


if __name__ == "__main__":
    create_app().run(debug=True)