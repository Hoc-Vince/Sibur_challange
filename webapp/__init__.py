from flask import Flask, flash, render_template, redirect, url_for 
from webapp.forecast.views import blueprint as forecast_blueprint


def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(forecast_blueprint)

    return app