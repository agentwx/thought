#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import base64
import tornado.web
from app.lib import router
from app import helper
from app.resperror import AuthError, DBError
from app.auth.models import User
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
    @helper.parse_json
    def post(self, *args, **kwargs):

        email = self.request.data['email']
        password = base64.b64decode(self.request.data['password'])

        user = User.findone(email=email)
        if user:
            result = dict(code=AuthError.user_has_exist.code, message=AuthError.user_has_exist.message)
        else:
            user = User(email=email, password=password)
            try:
                row = user.insert()
            except Exception, e:
                logger.error('insert db error {}'.format(e))
                result = dict(code=DBError.update_error.code, messge=DBError.update_error.message)
            else:
                if row:
                    self.set_status(201)
                    result = {}
                else:
                    self.set_status(500)
                    result = dict(code=DBError.insert_error.code, messge=DBError.insert_error.message)
        self.jsonify(result)


@router.Route('/api/v1/auth/logout')
class ApiAuthLogoutHandler(helper.BaseApiRequestHandler):
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        self.session.pop('user')
        result = {'message': u'logout successful'}
        self.jsonify(result)
