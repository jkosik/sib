from flask import Blueprint, render_template
from portal.database.models import TargetSet, Target
from werkzeug import abort 

query = Blueprint('query', __name__) 

@query.route("/query")
def req():
    return render_template('query.html')

 
