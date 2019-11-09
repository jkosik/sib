from flask import Blueprint, render_template, request
from portal.query.models import CHECKS 
from werkzeug import abort 

query = Blueprint('query', __name__) 

@query.route("/request")
def req():
    req = request.args.get('req', 'default')
    return render_template('request.html', req=req)

@query.route('/response')  
def res(): 
    return render_template('response.html', res=CHECKS)
 
@query.route('/response/<key>') 
def get_check(key):
    check = CHECKS.get(key) # CHECKS[key] will fail here when key does not exist
    print(f'Check value is {key}')
    if not check:
        return abort(404)
    else: 
        return render_template('response.html', check=check)        
 
#@query.route('/add/<key>/<type>') 
#def get_type(key, type): 
    #CHECKS[key] = message #update in-memory data
#    return CHECKS[key]