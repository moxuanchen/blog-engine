# -*- coding: utf-8 -*-

from flask import Blueprint
from flask.ext.restful import Api
from flask.ext.restful import Resource
from traceback import print_exc

from core.models import User
from core.models import db

blueprint = Blueprint("demo", __name__)
api = Api(blueprint)


class GetUserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.__repr__()
        else:
            return "ID: %d not exist..." % id


class GetUserByName(Resource):
    def get(self, name):
        user = User.query.filter_by(name=name).first()
        if user:
            return user.__repr__()
        else:
            return "Name: %s not exist..." % name


class CreateUserByName(Resource):
    def get(self, name):
        try:
            db.session.add(User(name))
            db.session.commit()
        except Exception:
            print_exc()
        return "Create user(%s) success..." % name


api.add_resource(GetUserByID, '/user/get/<int:id>')
api.add_resource(GetUserByName, '/user/get/<name>')
api.add_resource(CreateUserByName, '/user/create/<name>')
