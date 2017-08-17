# _*_ encoding:utf-8 _*_
"""
前台初始化脚本
"""
from flask import Blueprint

home = Blueprint("home", __name__)

# 程序是从上倒下执行的，因为views用到了home，所以要先定义home，才能import
import app.home.views
