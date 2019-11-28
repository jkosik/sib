from portal import db
from flask import Blueprint, render_template, request, flash
from portal.database.models import TargetSet, Target, TargetSetForm, TargetForm

admin = Blueprint('admin', __name__) 

@admin.route("/admin", methods=['GET', 'POST'])
def add():
    form = TargetSetForm(csrf_enabled=True) 
    #if request.method == 'POST' and form.validate():
    if form.validate_on_submit(): #shorthanded "if request.method == 'POST' and form.validate():" incl. allowing PUT.
        name = form.name.data 
        if name:
            data = TargetSet(name) 
            db.session.add(data) 
            db.session.commit() 
            flash('Target Set has been added.') 
    #elif form.errors: #commented not to trigger errors across both forms. Solution: https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms
    #    flash(form.errors, 'danger')
    form2 = TargetForm(csrf_enabled=True) 
    #if request.method == 'POST' and form2.validate():
    if form2.validate_on_submit(): #shorthanded "if request.method == 'POST' and form.validate():" incl. allowing PUT
        target = form2.target.data 
        if target:
            targetset_id = form2.targetset.data.id 
            data = Target(target, targetset_id)             
            db.session.add(data) 
            db.session.commit() 
            flash('Target has been added.') 
    #elif form.errors: #commented not to trigger errors across both forms. Solution: https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms
    #    flash(form2.errors, 'danger')
    return render_template('admin.html', form=form, form2=form2)

