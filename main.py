#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'


import tornado.httpserver
import tornado.ioloop
from app import Application


def create_app():
    app = Application()
    return app

if __name__ == '__main__':
    app = create_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(5000)
    io_loop = tornado.ioloop.IOLoop.instance()
    io_loop.start()
