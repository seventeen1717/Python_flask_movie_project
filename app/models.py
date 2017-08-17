# _*_ encoding:utf-8 _*_
"""
models用来存放数据模型
"""
from _datetime import datetime
from app import db


# 定义模型
# 定义会员的数据模型
class User(db.Model):
    __tablename__ = "user"  # 要往数据库中存的表名称
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 帐号
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    info = db.Column(db.Text)  # 简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联
    comments = db.relationship('Comment', backref='user')  # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='user')  # 电影收藏外键关系关联

    # 定义返回类型
    def __repr__(self):
        return "<User %r>" % self.name

    # 检测密码
    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 定义会员登录日志数据模型
class Userlog(db.Model):
    __tablename__ = "userlog"  # 指定表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员编号
    ip = db.Column(db.String(100))  # 最近登录IP地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间

    # 在查询的时候返回一个格式
    def __repr__(self):
        return "<Userlog %r>" % self.id


# 定义标签数据模型
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 创建时间
    movies = db.relationship("Movie", backref='tag')  # 电影外键关系关联

    def __repr__(self):
        return "<Tag %r>" % self.name


# 定义电影数据模型
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 电影标题
    url = db.Column(db.String(255), unique=True)  # 电影地址
    info = db.Column(db.Text)  # 电影简介
    logo = db.Column(db.String(255), unique=True)  # 电影封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 电影播放量
    commentnum = db.Column(db.BigInteger)  # 电影评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))  # 地区
    release_time = db.Column(db.Date)  # 发布时间
    length = db.Column(db.String(100))  # 电影长度
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    comments = db.relationship("Comment", backref='movie')  # 评论关系关联
    moviecols = db.relationship("Moviecol", backref='movie')  # 电影收藏关系关联

    def __repr__(self):
        return "<Movie %r>" % self.title


# 定义上映预告数据模型
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 上映预告标题
    logo = db.Column(db.String(255), unique=True)  # 上映预告封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 创建时间

    def __repr__(self):
        return "<Preview %r>" % self.title


# 定义评论数据模型
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 评论内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间

    def __repr__(self):
        return "<Comment %r>" % self.id


# 定义电影收藏数据模型
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# 定义权限数据模型
# url地址就是表示路由里面的地址，如果路由的地址和权限的地址匹配说明这个管理员有权限，如何过不匹配则说明那个没权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 创建时间

    def __repr__(self):
        return "<Auth %r>" % self.name


# 定义角色数据模型
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600), unique=True)  # 权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 创建时间
    admins = db.relationship("Admin", backref='role')  # 管理员外键关系关联

    def __repr__(self):
        return "<Role %r>" % self.name


# 定义管理员数据模型
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员名称
    pwd = db.Column(db.String(100))  # 密码
    is_super = db.Column(db.SmallInteger)  # 是否是超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 角色编号
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 创建时间
    adminlogs = db.relationship("Adminlog", backref='admin')  # 管理员登录日志外键关系关联
    oplogs = db.relationship("Oplog", backref='admin')  # 操作日志外键关系关联

    def __repr__(self):
        return self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 定义管理员登录日志数据模型
class Adminlog(db.Model):
    __tablename__ = "adminlog"  # 指定表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员编号
    ip = db.Column(db.String(100))  # 最近登录IP地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间

    # 在查询的时候返回一个格式
    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 定义操作日志数据模型
class Oplog(db.Model):
    __tablename__ = "oplog"  # 指定表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员编号
    ip = db.Column(db.String(100))  # 操作IP地址
    reason = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 创建时间

    # 在查询的时候返回一个格式
    def __repr__(self):
        return "<Oplog %r>" % self.id

# if __name__ == "__main__":
#     # db.create_all()
#
#     role=Role(
#         name="超级管理员",
#         auths=""
#     )
#     db.session.add(role)
#     db.session.commit()
#     from werkzeug.security import generate_password_hash
#
#     admin=Admin(
#         name="imoocmovie",
#         pwd=generate_password_hash("imoocmovie"),
#         is_super=0,
#         role_id=1
#     )
#     db.session.add(admin)
#     db.session.commit()
