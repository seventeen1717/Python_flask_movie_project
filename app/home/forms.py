# _*_ encoding:utf-8 _*_
"""
前台表单处理文件
"""
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError

from app.models import User


class RegistForm(FlaskForm):
    # 昵称
    name = StringField(
        # 标签
        label="昵称",
        # 验证器
        validators=[
            DataRequired("请输入昵称！")
        ],
        # 描述
        description="昵称",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！"
        }
    )
    # 邮箱
    email = StringField(
        # 标签
        label="邮箱",
        # 验证器
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确!")
        ],
        # 描述
        description="邮箱",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！"
        }
    )
    # 手机
    phone = StringField(
        # 标签
        label="手机",
        # 验证器
        validators=[
            DataRequired("请输入手机！"),
            Regexp('1[3458]\\d{9}', message='手机格式不正确!')
        ],
        # 描述
        description="手机",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机！"
        }
    )
    # 密码
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
            # "required": "required",
        },
    )
    # 确认密码
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('pwd', message='两次密码不一致!')
        ],
        description="确认密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入确认密码！"
        }
    )
    # 注册
    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        },
    )

    # 验证
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已经存在!")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在!")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号码已经存在!")


# 会员登录表单
class LoginForm(FlaskForm):
    # 帐号
    name = StringField(
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
            "class": "form-control input-lg",
            "placeholder": "请输入帐号！"
        }
    )
    # 密码
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！"
        },
    )
    # 登录
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        },
    )

    # def validate_name(self, field):
    #     name = field.data
    #     user = User.query.filter_by(name=name).count()
    #     if user == 0:
    #         raise ValidationError("会员帐号不存在!")

    # def validate_pwd(self, field):
    #     from app.models import User
    #     pwd = field.data
    #     name = self.name.data
    #     print(name)
    #     user = User.query.filter_by(name=name).first()
    #     if not user.check_pwd(pwd):
    #         raise ValidationError("密码错误!")


# 会员中心修改资料表单
class UserdetailForm(FlaskForm):
    # 昵称
    name = StringField(
        # 标签
        label="昵称",
        # 验证器
        validators=[
            DataRequired("请输入昵称！")
        ],
        # 描述
        description="昵称",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入昵称！"
        }
    )
    # 邮箱
    email = StringField(
        # 标签
        label="邮箱",
        # 验证器
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确!")
        ],
        # 描述
        description="邮箱",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！"
        }
    )
    # 手机
    phone = StringField(
        # 标签
        label="手机",
        # 验证器
        validators=[
            DataRequired("请输入手机！"),
            Regexp('1[3458]\\d{9}', message='手机格式不正确!')
        ],
        # 描述
        description="手机",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机！"
        }
    )
    # 头像
    face = FileField(
        label="头像",
        # 验证器
        validators=[
            DataRequired("请上传头像！")
        ],
        # 描述符
        description="头像",
    )
    # 简介
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
    # 按钮
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success",
        },
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
        '修改密码',
        render_kw={
            "class": "btn btn-success",
        }
    )


# 电影评论表单
class CommentForm(FlaskForm):
    # 评论内容
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容！")
        ],
        description="内容",
        render_kw={
            "id": "input_content"
        }

    )
    # 按钮
    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )
