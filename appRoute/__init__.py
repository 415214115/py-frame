from flask import Flask, request
# from dbSQL.db import app
from appRoute.apiRouter import api

from datetime import timedelta

import os

# from flask_cors import CORS
from flask_cors import *

def creat_app():
    app = Flask(__name__)

    # CORS(app, resources={r"/*": {"origins": "*"}})
    CORS(app, supports_credentials=True)


    app.debug = True

    # app.config.from_object(Config())

    app.config['SECRET_KEY'] = os.urandom(24)

    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10) # 设置session到期时间
    # session.permanent = True

    # # 配置数据库
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:scw729295@127.0.0.1/test"
    # # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


  
        



    api.init_app(app)
    return app


# 使用session的加密秘钥
# class Config(object):
#     SECRET_KEY = "DJFAJLAJAFKLJQ"