# _*_ encoding:utf-8 _*_

from app import db
from app.models import Role,Admin

role = Role(
    name="超级管理员",
    auths=""
)
db.session.add(role)
db.session.commit()
from werkzeug.security import generate_password_hash

admin = Admin(
    name="imoocmovie",
    pwd=generate_password_hash("imoocmovie"),
    is_super=0,
    role_id=1
)
db.session.add(admin)
db.session.commit()
