from portal import db
from flask import Blueprint, render_template, request, flash
from portal.database.models import TargetSet, Target, TargetSetForm

admin = Blueprint('admin', __name__) 

@admin.route("/admin", methods=['GET', 'POST'])
def add_targetset():
    form = TargetSetForm(csrf_enabled=False) 
 
    if request.method == 'POST':
        name = form.name.data 
        data = TargetSet(name) 
        db.session.add(data) 
        db.session.commit() 
        flash('Target Set has been added.') 
    return render_template('admin.html', form=form)

 
