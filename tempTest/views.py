#encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .form import UserRegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'tempTest/index.html')


def user_register(request):
    if request.method =='POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']#通过key取到页面的值
            password = user_form.cleaned_data['password']#拿到页面填写的值
            email = user_form.cleaned_data['email']
            #TODO 入库前的校验，保证用户没有重复注册
            User.objects.create_user(username, email, password)#插入并保存到数据库
            return HttpResponseRedirect('../login')#登录页面
    else:
        user_form =UserRegisterForm()
    return render(request, 'tempTest/register.html',{'user':user_form})

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取登录页面提交的用户名和密码
            user_name = login_form.cleaned_data['username']
            user_pwd = login_form.cleaned_data['password']
            # TODO 没有判断是否已经登录
            # 校验用户名和密码, 连个返回值，USER, NONE
            user = authenticate(username=user_name, password=user_pwd)
            if user:
                login(request, user)  # 登录
                return HttpResponseRedirect('../index')
            else:
                return HttpResponse('用户名或密码错误！！')
    else:
        login_form = LoginForm()  # 相当于get 请求，直接渲染页面
    return render(request, 'tempTest/login.html', {'user': login_form})

# 注销
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('index')


def show_image(request):
    return render(request, 'tempTest/show.html')
