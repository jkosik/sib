from portal import db
from flask import Blueprint, render_template, request, jsonify
from portal.database.models import Assets

asset = Blueprint('asset', __name__) 

@asset.route('/asset/list')
def asset_list():
    assets = Assets.query.all()
    res = {}
    for asset in assets:
        res[asset.id] = {
            'ipset': asset.ipset
        }
    #return jsonify(res)
    return render_template("asset.html", res=res)

@asset.route('/asset/add', methods=['POST',]) 
def asset_add(): 
    ipset = request.form.get('ipset') 
    asset = Assets(ipset) 
    db.session.add(asset) 
    db.session.commit() 
    return 'Asset added.' 



