#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import tornado.web
from app.lib import router
from app import helper
from settings import logger

__author__ = 'ghost'


@router.Route('/api/v1/auth/login')
class ApiAuthLoginhandler(helper.BaseApiRequestHandler):

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        email = data['email']
        password = data['password']
        if email == 'rsj217@gmail.com' and password == '123':
            self.session['user'] = 'rsj217'
            self.session.save()
            result = {'message': u'login successful'}
        else:
            self.set_status(401)
            result = {'message': u'username or password error'}
        self.jsonify(result)


@router.Route('/api/v1/auth/register')
class ApiAuthRegisterHandler(helper.BaseApiRequestHandler):

    def post(self, *args, **kwargs):
        result = {'message': u'username or password error'}
        self.jsonify(result)


@router.Route('/api/v1/auth/logout')
class ApiAuthLogoutHandler(helper.BaseApiRequestHandler):
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        self.session.pop('user')
        result = {'message': u'logout successful'}
        self.jsonify(result)
