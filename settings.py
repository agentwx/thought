#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'

import logging
import redis
import tornado.util
from tornado.options import define, options
from app.lib.session import SessionManager
from app.lib.torndb import Connection


define('env', default='dev')
define('port', default=5000)
options.parse_command_line()

if options.env == 'dev':
    config = tornado.util.import_object('config.dev')
elif options.env == 'pro':
    config = tornado.util.import_object('config.pro')
elif options.env == 'test':
    config = tornado.util.import_object('config.test')


def create_redis():
    """ 创建 redis 连接 """
    connection_pool = redis.ConnectionPool(
        host=config.REDISDB['host'],
        port=config.REDISDB['port'],
        db=config.REDISDB['db'],
        password=config.REDISDB['password']
    )

    return redis.Redis(connection_pool=connection_pool)


def create_mysqldb():
    """ 创建 mysql 连接 """
    mdb = Connection(
        config.MYSQLDB['host'],
        config.MYSQLDB['db'],
        config.MYSQLDB['user'],
        config.MYSQLDB['password'],
    )
    return mdb

def create_log():
    logger = logging.getLogger(config.LOGGER_NAME)
    logger.setLevel(config.LOGGER_LEVEL)
    return logger

def create_session_manager():
    redis_conf = {
        'host': config.REDISDB['host'],
        'port': config.REDISDB['port'],
        'password': config.REDISDB['password'],
        'db': config.REDISDB['db']
    }
    return SessionManager("session_secret", redis_conf, 30 * 24 * 60 * 60)


logger = create_log()
session_manager = create_session_manager()
logger.info('setting session manager conn {}'.format(id(session_manager)))

db = create_mysqldb()
logger.info('setting db conn {}'.format(id(db)))