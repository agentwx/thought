# !/usr/bin/env python
# -*- coding:utf-8 -*-


from collections import namedtuple

__author__ = 'ghost'

Error = namedtuple('Error', ['code', 'message'])


class RespError(object):
    json_error = Error(code=400900, message=u'invalid json params')
    token_missing = Error(code=40901, message=u'missing the token')

class AuthError(object):
    user_not_exist = Error(code=400100, message=u'the user doest not exist')
    user_has_exist = Error(code=400101, message=u'the user has exist')
    username_invalid = Error(code=400102, message=u'username must be more than 6 character')
    passwd_error = Error(code=400103, message=u'password error')
    passwd_invalid = Error(code=400104, message=u'password must be 6 ~ 24 letters and numbers')
    email_error = Error(code=400104, message=u'invalid email')
    email_length = Error(code=400105, message=u'email must less than 60 character')


class DBError(object):

    update_error = Error(code=400801, message=u'db update error')
    insert_error = Error(code=400802, message=u'db insert error')