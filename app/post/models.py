# !/usr/bin/env python
# -*- coding:utf-8 -*-


from app.lib.tornorm import Model, Integer, String

__author__ = 'ghost'


class Post(Model):
    __table__ = 'post'

    id = Integer(length=10, primary_key=True)
    user_id = Integer(length=10)
    text = String(length=270)