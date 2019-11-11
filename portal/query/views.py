from flask import Blueprint, render_template
from portal.database.models import TargetSet, Target

query = Blueprint('query', __name__) 

@query.route("/query")
def req():
    return render_template('query.html')

 
