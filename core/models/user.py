# -*- coding: utf-8 -*-

from database import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.id:
            return '<User: id=%d, name=%s>' % (self.id, self.name)
        else:
            return '<User: id=None, name=%s>' % self.name
