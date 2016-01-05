#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'

import os
import logging

DEPLOY = 'development'

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SETTINGS = {
    "debug": True,
    "template_path": os.path.join(PROJECT_ROOT, "templates"),
    "static_path": os.path.join(PROJECT_ROOT, "static"),
    "cookie_secret": "you_never_guess",
    "login_url": "/auth/login",
    # "admin_login_url": "/admin/login",
    "xsrf_cookies": True
}

MYSQLDB = {
    'host': '127.0.0.1',
    'db': 'stock_localhost',
    'user': 'root',
    'password': ''
}

REDISDB = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 9,
    'password': ''
}

LOGGER_NAME = 'thought'
LOGGER_LEVEL = logging.DEBUG
ORM_LOGGER_LEVEL = logging.INFO
