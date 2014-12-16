# -*- coding: utf8 -*-
from threading import Thread

__author__ = 'omri'
from app import db, models

# u = models.User(nickname='john', email='john@email.com')
# db.session.add(u)
# db.session.commit()
#
# u = models.User(nickname='susan', email='susan@email.com')
# db.session.add(u)
# db.session.commit()

users = models.User.query.all()
print users
posts = models.Post.query.all()
print posts

# f = models.followers
# print f.get(1)


# for u in users:
#     print(u.id,u.nickname, u.email)

# import datetime
# u = models.User.query.get(1)
# p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
# db.session.add(p)
# db.session.commit()

# user = models.User.query.get(1)
# print user.nickname
# user.nickname = 'omri saadon'
#
# db.session.commit()
# print user.nickname
# users = models.User.query.all()
# for u in users:
#     db.session.delete(u)
# posts = models.Post.query.all()
# for p in posts:
#     db.session.delete(p)
# db.session.commit()


#get all posts from a user
# u = models.User.query.all()
# print u

#
#
# # obtain author of each post
# posts = models.Post.query.all()
# for p in posts:
#     print p.language
#
# # a user that has no posts
# u = models.User.query.get(2)
# print u
# print u.posts.all()
#
#
# # get all users in reverse alphabetical order
# print models.User.query.order_by('nickname desc').all()

# from app.models import Post
# from app import db
# for post in Post.query.all():
#    db.session.delete(post)
# db.session.commit()


# from flask.ext.mail import Message
# from app import app, mail
# from config import ADMINS
# msg = Message('test subject', sender=ADMINS[0], recipients=ADMINS)
# msg.body = 'text body'
# msg.html = '<b>HTML</b> body'
#
#
# def send_async_email(msg):
#     with app.app_context():
#         print msg
#         mail.send(msg)
#
# thr = Thread(target=send_async_email(msg), args=app.app_context())
#

from app import translate
print translate.microsoft_translate('Hi, how are you?', 'en', 'he')
