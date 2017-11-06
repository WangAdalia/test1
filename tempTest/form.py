#encoding: utf-8
from django import forms  #所有form表格的父类
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20,label='用户名')
    password = forms.CharField(max_length=16,label='密码')
    email = forms.EmailField(label='邮箱')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='用户名')
    password = forms.CharField(max_length=10, label='密码')