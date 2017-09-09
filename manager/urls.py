from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$',views.home,name="home"),
	url(r'^addband/$',views.addBand,name="addband"),
	#url(r^display Band Name in url
] 

