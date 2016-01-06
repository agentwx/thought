# !/usr/bin/env python
# -*- coding:utf-8 -*-


from app.lib.tornorm import Model, Integer, String

__author__ = 'ghost'


class User(Model):
    __table__ = 'user'

    id = Integer(length=10, primary_key=True)
    nickname = String(length=20)
    phone = String(length=11)
    email = String(length=40, nullable=False)
    password = String(length=60, nullable=False)

    # def __repr__(self):
    #     return '<User {}>'.format(self.nickname)