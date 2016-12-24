from fired import app, db
from fired.models.user.models import User
from flask import request, jsonify
from werkzeug.exceptions import abort


@app.route("/api/v1/users/", methods=['POST'])
def create():
    user = User()
    if request.data:
        user.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json()
    return abort(400)


@app.route("/api/v1/users/<int:id>/", methods=['GET'])
def read(id):
    user = User.query.get_or_404(id)
    return user.to_json()


@app.route("/api/v1/users/<int:id>/", methods=['PUT', 'PATCH'])
def update(id):
    user = User.query.get_or_404(id)
    if request.data:
        data = request.get_json()
        for key in data:
            if key in ['username', 'phone', 'email', 'password']:
                user.__setattr__(key, data[key])
        db.session.commit()
        user = db.session.query(User).get(id)  # need to get the user again because sqlalchemy things
    return user.to_json()


@app.route("/api/v1/users/<int:id>/", methods=['DELETE'])
def delete(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify()
