from portal import db
from flask import Blueprint, render_template, request, jsonify, flash
from portal.database.models import TargetSet, Target
from sqlalchemy import func

target = Blueprint('target', __name__) 

@target.route('/target/list')
def targetset_list():
    flash('List of existing Target Sets', 'success')
    # main query
    targetsets = TargetSet.query.all()
    
    # summarize occurrences of targetset_id in Target table and format to json to enrich res output. Aka merging TargetSet and Target
    count = Target.query.with_entities(Target.targetset_id, func.count(Target.targetset_id)).group_by(Target.targetset_id).all() # outputs [(1,3),(2.7)]
    print('counts: ', count)
    count_jsonlist = []
    for item in count:
        json_element = {
            'ts_id': item[0],
            'ts_count': item[1]
        }
        count_jsonlist.append(json_element.copy())
    print('count_jsonlist: ', count_jsonlist)
    
    # append no. of occurrences to the main query 
    res = []
    for item in targetsets:
        c = 0 # var to store target count when targetset.id == count_jsonlist['ts_id']
        for cc in count_jsonlist:
            if cc['ts_id'] == item.id:
                c = cc['ts_count']
        json_element = {
            'id': item.id,
            'name': item.name,
            'count': c
        }
        res.append(json_element.copy())
    #return jsonify(res)
    return render_template("target.html", res=res)
    '''
    Pagination works smoothly on sql response objects. Here we have json output combining 2 queries. To utilize pagination, create complex sqlalchemy query
    equivalent to "# select targetset.id AS id, targetset.name AS name, count(target.targetset_id) AS count from targetset LEFT JOIN target ON targetset.id = target.targetset_id GROUP BY targetset.name;"
    and paginate as usual.
    '''


@target.route('/target/<key>', methods=['GET', 'POST']) 
def targetset_detail(key):
    targets = Target.query.filter_by(targetset_id = key).all()
    print(f'Targets in TS {key}: {targets}')
    return render_template('target-detail.html', targets=targets, ts=key)


