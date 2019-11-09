from flask import Blueprint, render_template, request
from portal.model_test.models import CHECKS 
from werkzeug import abort 

model_test = Blueprint('model_test', __name__) 

@model_test.route("/model_test/request")
def req():
    return render_template('request.html')

@model_test.route('/model_test/response')  
def res(): 
    return render_template('response.html', res=CHECKS)
 
@model_test.route('/model_test/response/<key>') 
def get_check(key):
    check = CHECKS.get(key) # CHECKS[key] will fail here when key does not exist
    print(f'Check value is {key}')
    if not check:
        return abort(404)
    else: 
        return render_template('response.html', check=check)        
 
