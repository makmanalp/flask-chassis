from flask import Flask

from raven.contrib.flask import Sentry
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.contrib.profiler import ProfilerMiddleware

from {{cookiecutter.app_name}}.views import CatAPI
from {{cookiecutter.app_name}}.views import api, cache
from {{cookiecutter.app_name}}.models import db


def create_app(config={}):
    app = Flask("{{cookiecutter.app_name}}")
    app.config.from_envvar("FLASK_CONFIG")
    app.config.update(config)

    #API Endpoints
    api.add_resource(CatAPI, "/cats/<int:cat_id>")

    #External
    sentry.init_app(app)
    api.init_app(app)
    cache.init_app(app)

    #Internal
    db.init_app(app)

    with app.app_context():
        db.create_all()

    #Debug tools
    if app.debug:
        DebugToolbarExtension(app)
        if app.config.get("PROFILE", False):
            app.wsgi_app = ProfilerMiddleware(app.wsgi_app,
                                              restrictions=[30],
                                              sort_by=("time", "cumulative"))

    return app

sentry = Sentry()
