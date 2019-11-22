# sib (Security Intelligence Browser)
Flask application for querying security intelligence databases 

# How to run
```
$ source venv/source/activate  
$ export FLASK_APP=run.py  
$ flask run  
```

# Virtual ENV
```
$ pip3 list

Package          Version
---------------- -------
alembic          1.3.0  
Click            7.0    
Flask            1.1.1  
Flask-Migrate    2.5.2  
Flask-SQLAlchemy 2.4.1  
itsdangerous     1.1.0  
Jinja2           2.10.3 
Mako             1.1.0  
MarkupSafe       1.1.1  
pip              19.3.1 
python-dateutil  2.8.1  
python-editor    1.0.4  
setuptools       41.6.0 
six              1.13.0 
SQLAlchemy       1.3.10 
Werkzeug         0.16.0 
wheel            0.33.6 
```

# Manual DB updates
```
$ python3
>>> import requests
>>> requests.post('http://127.0.0.1:5000/target/add-target-set', data={'name':'aaa'})
<Response [200]>
>>> requests.post('http://127.0.0.1:5000/target/add-target', data={'target':'1.1.1.1', 'targetset_id': '1'})
<Response [200]>
```
