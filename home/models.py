# -*- coding: utf-8 -*-
"""
    flaskbb.user.models
    ~~~~~~~~~~~~~~~~~~~

    This module provides the models for the user.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
from flask_login import UserMixin, AnonymousUserMixin

from extensions import db
from exceptions import AuthenticationError
from utils.database import CRUDMixin, UTCDateTime


class User(db.Model, UserMixin, CRUDMixin):
    __tablename__ = "users"

    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    verified = db.Column(db.Boolean)
    pwd = db.Column('password', db.String(120))
    username = db.Column(db.String(20))
    usernameRaw = db.Column(db.String(20))
    createTime = db.Column(db.DateTime)

    # 用户头像
    logo = db.Column(db.String(200))
    # 用户主题
    theme = db.Column(db.String(200))

    # 用户配置
    notebookWidth = db.Column(db.Integer)
    noteListWidth = db.Column(db.Integer)
    mdEditorWidth = db.Column(db.Integer)
    leftIsMin = db.Column(db.Boolean)

    # 第三方登录
    thirdUserId = db.Column(db.String(200))
    thirdUsername = db.Column(db.String(200))
    thirdType = db.Column(db.Integer)

    # 用户的账户类型
    imageNum = db.Column(db.Integer)
    imageSize = db.Column(db.Integer)
    attachNum = db.Column(db.Integer)
    attachSize = db.Column(db.Integer)
    fromUserId = db.Column(db.String(200))

    accountType = db.Column(db.String(200))
    accountStartTime = db.Column(db.DateTime)
    accountEndTime = db.Column(db.DateTime)

    # 阈值
    maxImageNum = db.Column(db.Integer)
    maxImageSize = db.Column(db.Integer)
    maxAttachNum = db.Column(db.Integer)
    maxAttachSize = db.Column(db.Integer)
    maxPerAttachSize = db.Column(db.Integer)

    # updateSequenceNum,全局的
    usn = db.Column(db.Integer)
    # 需要全量同步的时间，如果>客户端的LastSyncTime, 则需要全量更新
    fullSyncBefore = db.Column(db.DateTime)
