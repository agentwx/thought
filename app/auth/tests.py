#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'

import unittest
import base64
import requests

HOST = 'http://127.0.0.1:5000'


class TestRegister(unittest.TestCase):
    def setup(self):
        pass

    def test_post(self):
        data = {
            'email': 'rsj217@gmail.com',
            'password': base64.b64encode('123qwe')
        }
        url = '{}/api/v1/auth/register'.format(HOST)
        resp = requests.post(url, json=data)
        print resp.json()
        self.assertEqual(201, resp.status_code)
