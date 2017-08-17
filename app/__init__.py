# _*_ encoding:utf-8 _*_
"""
app初始化文件
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

# 实例化flask
app = Flask(__name__)
# 使用app来调用一个config对象
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mysql123@127.0.0.1:3306/movie"
# SQLALCHEMY_TRACK_MODIFICATIONS如果设置为True,就会追踪对象的修改并且发送信号
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'e5365845231643ab92055e277a7f45a3'
# 定义文件上传的路径
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")

# 实例化flask
# app = Flask(__name__)

# 开启调试模式
app.debug = True

# 定义db对象
# 实例化SQLAlchemy，传入app对象
db = SQLAlchemy(app)

# 导入蓝图对象
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)  # home代表前台，就不需要加上url前缀了
app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 为了区分路由，加个url前缀


# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
