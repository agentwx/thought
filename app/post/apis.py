#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from app import helper
from app.resperror import DBError
from app.lib import router
from app.post.models import Post
from settings import logger


__author__ = 'ghost'


@router.Route('/api/v1/post/add')
class ApiPostAddHandler(helper.BaseApiRequestHandler):

    @tornado.web.authenticated
    @helper.parse_json
    def post(self, *args, **kwargs):
        text = self.request.data['text']

        post = Post(text=text, user_id=self.session['id'])
        try:
            row = post.insert()
        except Exception, e:
            logger.error('insert db error {}'.format(e))
            self.set_status(500)
            result = dict(code=DBError.update_error.code, messge=DBError.update_error.message)
        else:
            if row:
                self.set_status(201)
                result = {}
            else:
                self.set_status(500)
                result = dict(code=DBError.insert_error.code, messge=DBError.insert_error.message)
        self.jsonify(result)
