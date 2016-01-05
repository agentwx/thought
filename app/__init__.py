#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop
from app.thought.views import *
from app.auth.views import *
from app.auth.apis import *
from app.lib import router
from settings import logger, db, config, session_manager

__author__ = 'ghost'


class Application(tornado.web.Application):
    @staticmethod
    def ping_db():
        logger.info('ping mysql db conn {}'.format(id(db)))
        db.query('SHOW VARIABLES')
        logger.warning('ping databases ... ...')

    def __init__(self):
        super(Application, self).__init__(
                handlers=router.Route.get_routes(),
                **config.SETTINGS
        )
        logger.info('init the db conn {}'.format(id(db)))

        self.session_manager = session_manager
        tornado.ioloop.PeriodicCallback(self.ping_db, 60 * 1000).start()
