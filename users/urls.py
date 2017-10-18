from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login,logout
from users import views

urlpatterns = [
    url(r'^login/$',login,name="login"),
    url(r'^logout/$',logout,name="logout"),
    url(r'^register/$',views.register,name="register")
]
