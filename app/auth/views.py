#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from app.lib import router
from app import helper

__author__ = 'ghost'


@router.Route('/auth/login')
class AuthLoginHandler(helper.BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render('auth/login.html')


@router.Route('/auth/register')
class AuthRegisterHandler(helper.BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render('auth/register.html')


@router.Route('/auth/logout')
class AuthLogoutHandler(helper.BaseRequestHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.session.pop('user')
        self.session.save()
        result = {'message': u'logout successful'}
        self.redirect('/')
