#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import base64
import tornado.web
from app.lib import router
from app import helper
from app.resperror import AuthError, DBError, RespError
from app.auth.models import User
from settings import logger

__author__ = 'ghost'


@router.Route('/api/v1/auth/login')
class ApiAuthLoginhandler(helper.BaseApiRequestHandler):

    def get(self, *args, **kwargs):
        authorization = self.request.headers.get('Authorization')
        if authorization:
            token = authorization[6:]
            email, password = base64.b64decode(token).split(':')
        else:
            self.set_status(400)
            result = dict(code=RespError.token_missing.code, message=RespError.token_missing.message)
            return self.jsonify(result)

        user = User.findone(email=email)
        if not user:
            self.set_status(401)
            result = dict(code=AuthError.user_not_exist.code, message=AuthError.user_not_exist.message)
            return self.jsonify(result)

        if password == user.password:
            self.session['id'] = user.id
            if user.nickname:
                self.session['user'] = user.nickname
            else:
                self.session['user'], _ = user.email.split('@')
            self.session.save()
            result = {}
        else:
            self.set_status(401)
            result = dict(code=AuthError.passwd_error.code, message=AuthError.passwd_error.message)
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
        self.session.pop('id')
        result = {'message': u'logout successful'}
        self.jsonify(result)
