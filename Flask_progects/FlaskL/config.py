# -*- coding: utf-8 -*-


class Configure(object):
    DEBUG = True
    SECRET_KEY = 'password'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False