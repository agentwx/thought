# !/usr/bin/env python
# -*- coding:utf-8 -*-


from app.lib.tornorm import Model, Integer, String

__author__ = 'ghost'


class User(Model):
    __table__ = 'user'

    id = Integer(length=10, primary_key=True)
    nickname = String(length=10, nullable=False)
    phone = String(length=10, nullable=False)
    email = String(length=40)
    password = String(length=60)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)
