from os import path
from flask import Flask

from models.base import db
from resources import set_resources_in_app


def create_api(mode='development'):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)),
        '{}_instance'.format(mode)
    )

    app = Flask(
        __name__,
        instance_path=instance_path
    )

    app.config.from_object('configdb')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    set_resources_in_app(app)
    db.init_app(app=app)
    return app
