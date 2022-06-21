from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length,Email,EqualTo,ValidationError
from flaskblog.models import User
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=8),EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'{username.data} is already taken!')

    def validate_email(self, email):
        Email = User.query.filter_by(email = email.data).first()
        if Email:
            raise ValidationError(f'{email.data} is already taken!')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(f'{username.data} is already taken!')

    def validate_email(self, email):
        if email.data != current_user.email:
            Email = User.query.filter_by(email = email.data).first()
            if Email:
                raise ValidationError(f'{email.data} is already taken!')

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')
    
class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if not user:
            raise ValidationError(f'{email.data} has no account!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=8),EqualTo('password')])
    submit = SubmitField('Reset Password')