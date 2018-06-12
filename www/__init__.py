# -*- coding: utf-8 -*-

from flask import Flask, g

from www import views, extensions

APP_NAME = __name__

ROUTES = (
    (["/", "/hide"], views.hide.HideView),
)

def create_app(config=None):

    app = Flask(APP_NAME)

    configure_extensions(app)
    configure_routes(app, ROUTES)

    return app

def configure_routes(app, routes):
    
    for urls, view_class in routes:
        myview = view_class.as_view(view_class.getView())
        for url in urls:
            app.add_url_rule(url, view_func=myview)

def configure_extensions(app):
    pass

