from django.conf.urls import url
from .views import index,user_register,user_login,user_logout,show_image

urlpatterns = [
    url(r'^index/',index),
    url(r'^register', user_register, name='register'),
    url(r'^login', user_login, name='login'),
    url(r'^logout', user_logout, name='logout'),
    url(r'^show/', show_image, name='show_image'),


]