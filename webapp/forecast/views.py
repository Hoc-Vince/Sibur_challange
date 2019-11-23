from flask import abort, Blueprint, current_app, flash, render_template, redirect, request, url_for

blueprint = Blueprint('forecast', __name__)

@blueprint.route('/forecast', methods = ['GET','POST'])
def forecast():
    return render_template('forecast/index.html')