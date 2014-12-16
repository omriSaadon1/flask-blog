# -*- coding: utf-8 -*-
__author__ = 'omri'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('omri saadon')
MAIL_PASSWORD = os.environ.get('hbsvasermil')

# administrator list
ADMINS = ['omrisa25@gmail.com']

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = '9ad069dc-6308-49df-a32b-639f4ee1d6c7' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'umVIALZ+PYdo0xDi4ZYMdYPYOuj1Zy9BaY+PjUTTrnY=' # enter your MS translator app secret here

LANGUAGES = {
    'en': 'English',
    'es': 'Español',
}