from portal import db
from flask import Blueprint, render_template, request, flash
from portal.database.models import TargetSet, Target, TargetSetForm, TargetForm

admin = Blueprint('admin', __name__) 

@admin.route("/admin", methods=['GET', 'POST'])
def add():
    form = TargetSetForm(csrf_enabled=False) 
    if request.method == 'POST':
        name = form.name.data 
        if name:
            data = TargetSet(name) 
            db.session.add(data) 
            db.session.commit() 
            flash('Target Set has been added.') 
    form2 = TargetForm(csrf_enabled=False) 
    if request.method == 'POST':
        target = form2.target.data 
        if target:
            targetset_id = form2.targetset.data.id 
            data = Target(target, targetset_id)             
            db.session.add(data) 
            db.session.commit() 
            flash('Target has been added.') 
    return render_template('admin.html', form=form, form2=form2)

