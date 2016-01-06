#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from app.lib import router
from app import helper

__author__ = 'ghost'


@router.Route('/')
class ThoughtIndexHandler(helper.BaseRequestHandler):

    def get(self, *args, **kwargs):
        self.render('thought/index.html')

@router.Route('/home')
class ThoughtHomeHandler(helper.BaseRequestHandler):

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        user = self.session['user']
        self.render('thought/home.html', user=user)

