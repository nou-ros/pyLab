from flask import Flask 

from flask_pymongo import PyMongo

# convert the bson into json
from bson.json_util import dumps

# to generate random id
from bson.objectid import ObjectId

# to converto to json, request - to make request in the server
from flask import jsonify, request

# hasing library
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'secretkey'

# configure database url
app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"

# connecting mongdb database to pymongo lib
mongo = PyMongo(app)


# making routes
@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and request.method == 'POST':
        #hashing the password
        _hashed_password = generate_password_hash(_password)

        # generating id in the user table
        id = mongo.db.user.insert({'name':_name, 'email':_email, 'pwd':_hashed_password})
        
        resp = jsonify("User added successfully")

        resp.status_code = 200

        return resp

    else:
        return not_found()

# find all the users
@app.route('/users')
def users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp

# find a specific user
@app.route('/users/<id>')
def user(id):
    users = mongo.db.user.find_one({'_id':ObjectId(id)})
    resp = dumps(users)
    return resp

# delete a user
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id':ObjectId(id)})
    resp = jsonify("User deleted successfully")

    resp.status_code = 200

    return resp

# update a user
@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)

        mongo.db.user.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
        {'$set':{'name':_name, 'email':_email, 'pwd':_hashed_password}})
        
        resp = jsonify("User has been updated")

        resp.status_code = 200

        return resp
        
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message':'Not found' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp

# running our app
if __name__ == "__main__":
    app.run(debug=True)
