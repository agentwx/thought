#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'

import json
import functools
import tornado.web
from app.resperror import RespError
from app.lib import session
from settings import logger


class BaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = session.Session(self.application.session_manager, self)

    def get_current_user(self):
        super(BaseRequestHandler, self).get_current_user()
        user = self.session.get('user')
        logger.info('{}: Login user {}'.format(self.__class__.__name__, user))
        if not user:
            return None
        return user

    def jsonify(self, data):
        self.finish(json.dumps(data))


class BaseApiRequestHandler(BaseRequestHandler):

    def check_xsrf_cookie(self):
        return True

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')
        self.set_header('Cache-Control', 'no-store')
        self.set_header('Pragma', 'no-store')


def parse_json(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
        except Exception, e:
            logger.error('invalid json params')
            self.set_status(500)
            result = dict(code=RespError.json_error.code, message=RespError.json_error.message)
            return self.jsonify(result)
        setattr(self.request, 'data', data)
        return method(self, *args, **kwargs)
    return wrapper