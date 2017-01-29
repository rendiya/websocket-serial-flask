from flask import Blueprint, render_template, abort,request,Response
import json
from app import app
view = Blueprint('homepage', __name__)

@view.route('/', defaults={'page': 'index'})
@view.route('/', methods = ['GET'])
def help():
    """API_sitemap."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[app.view_functions[rule.endpoint].__doc__] = 'http://localhost:5000{rule}'.format(rule=rule.rule)
    payload = json.dumps(func_list)
    return Response(payload, status=200, mimetype='application/json')

@view.route('/hua',methods=['GET'])
def hua():
	return "hua"