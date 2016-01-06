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