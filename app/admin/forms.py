# _*_ encoding:utf-8 _*_
"""
后台表单处理文件
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo

from app.models import Admin, Tag, Auth, Role

# 计算标签tags
tags = Tag.query.all()
# 查询权限
auth_list = Auth.query.all()
# 查询角色
role_list = Role.query.all()


# 登录表单
class LoginForm(FlaskForm):
    """
    管理员登录表单
    """
    # 帐号
    account = StringField(
        # 标签
        label="帐号",
        # 验证器
        validators=[
            DataRequired("请输入帐号！")
        ],
        # 描述
        description="帐号",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            # 必须项
            # "required": "required",
        },
    )
    # 密码
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            # "required": "required",
        },
    )
    # 登录
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        },
    )

    # 验证帐号密码
    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在！")


# 标签表单
class TagForm(FlaskForm):
    """
    标签管理表单
    """
    # 标题
    name = StringField(
        label="名称",
        # 验证器
        validators=[
            DataRequired("请输入标签！")
        ],
        # 描述符
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称!",
            # "required": "required",
        }
    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


# 电影表单
class MovieForm(FlaskForm):
    """
    电影管理表单
    """
    # 电影标题
    title = StringField(
        label="片名",
        # 验证器
        validators=[
            DataRequired("请输入片名！")
        ],
        # 描述符
        description="片名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片名!",
            # "required": "required",
        }
    )
    # 电影地址
    url = FileField(
        label="文件",
        # 验证器
        validators=[
            DataRequired("请上传文件！")
        ],
        # 描述符
        description="文件",
    )
    # 电影简介
    info = TextAreaField(
        label="简介",
        # 验证器
        validators=[
            DataRequired("请输入简介！")
        ],
        # 描述符
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": "10"
        }
    )
    # 电影封面
    logo = FileField(
        label="封面",
        # 验证器
        validators=[
            DataRequired("请上传封面！")
        ],
        # 描述符
        description="封面",
    )
    # 星级
    star = SelectField(
        label="星级",
        # 验证器
        validators=[
            DataRequired("请选择星级！")
        ],
        coerce=int,
        choices=[(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")],
        # 描述符
        description="星级",
        render_kw={
            "class": "form-control"
        }
    )
    # 所属标签
    tag_id = SelectField(
        label="标签",
        # 验证器
        validators=[
            DataRequired("请选择标签！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        # 描述符
        description="标签",
        render_kw={
            "class": "form-control"
        }
    )
    # 地区
    area = StringField(
        label="地区",
        # 验证器
        validators=[
            DataRequired("请输入地区！")
        ],
        # 描述符
        description="地区",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区!"
        }
    )
    # 发布时间
    release_time = StringField(
        label="上映时间",
        # 验证器
        validators=[
            DataRequired("请选择上映时间！")
        ],
        # 描述符
        description="上映时间",
        render_kw={
            "class": "form-control",
            "placeholder": "请选择上映时间!",
            "id": "input_release_time",
        }
    )
    # 电影长度
    length = StringField(
        label="片长",
        # 验证器
        validators=[
            DataRequired("请输入片长！")
        ],
        # 描述符
        description="片长",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片长!"
        }
    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


# 预告表单
class PreviewForm(FlaskForm):
    # 预告标题
    title = StringField(
        label="预告标题",
        # 验证器
        validators=[
            DataRequired("请输入预告标题！")
        ],
        # 描述符
        description="预告标题",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入预告标题!",
            # "required": "required",
        }
    )
    # 预告封面
    logo = FileField(
        label="预告封面",
        # 验证器
        validators=[
            DataRequired("请上传预告封面！")
        ],
        # 描述符
        description="预告封面",
    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


# 修改密码表单
class PwdForm(FlaskForm):
    # 旧密码
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("请输入旧密码！")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码！"
        },
    )
    # 新密码
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("请输入新密码！")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码！"
        },
    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session["admin"]
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(pwd):
            raise ValidationError("旧密码错误!")


# 权限表单
class AuthForm(FlaskForm):
    # 权限名称
    name = StringField(
        label="权限名称",
        # 验证器
        validators=[
            DataRequired("请输入权限名称！")
        ],
        # 描述符
        description="权限名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入权限名称!"
        }
    )
    # 权限地址
    url = StringField(
        label="权限地址",
        # 验证器
        validators=[
            DataRequired("请输入权限地址！")
        ],
        # 描述符
        description="权限地址",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入权限地址!"
        }
    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


# 角色表单
class RoleForm(FlaskForm):
    # 角色名称
    name = StringField(
        label="角色名称",
        # 验证器
        validators=[
            DataRequired("请输入角色名称！")
        ],
        # 描述符
        description="角色名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入角色名称!"
        }
    )
    auths = SelectMultipleField(
        label="权限列表",
        # 验证器
        validators=[
            DataRequired("请选择权限列表！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in auth_list],
        # 描述符
        description="权限列表",
        render_kw={
            "class": "form-control"
        }
    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


# 管理员表单
class AdminForm(FlaskForm):
    # 管理员名称
    name = StringField(
        # 标签
        label="管理员名称",
        # 验证器
        validators=[
            DataRequired("请输入管理员名称！")
        ],
        # 描述
        description="管理员名称",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员名称！"
        },
    )
    # 管理员密码
    pwd = PasswordField(
        label="管理员密码",
        validators=[
            DataRequired("请输入管理员密码！")
        ],
        description="管理员密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员密码！"
        },
    )
    # 管理员重复密码
    repwd = PasswordField(
        label="管理员重复密码",
        validators=[
            DataRequired("请输入管理员重复密码！"),
            EqualTo('pwd', message="两次密码不一致!")
        ],
        description="管理员重复密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员重复密码！"
        },
    )
    # 所属角色
    role_id = SelectField(
        label="所属角色",
        # validators=[
        #     DataRequired("请选择所属角色！")
        # ],
        coerce=int,
        choices=[(v.id, v.name) for v in role_list],
        render_kw={
            "class": "form-control"
        }

    )
    # 按钮
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )
