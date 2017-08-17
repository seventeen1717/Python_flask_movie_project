# _*_ encoding:utf-8 _*_
"""
后台初始化脚本
"""
from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views
