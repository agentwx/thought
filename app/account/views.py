#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from app import helper
from app.lib import router



__author__ = 'ghost'


@router.Route('/home')
class AccountHomeHandler(helper.BaseRequestHandler):

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        user = self.session['user']
        self.render('account/home.html', user=user)

