from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$',views.home,name="home"),
	url(r'^addband/$',views.addBand,name="addband"),
	url(r'^success$',views.success,name="success"),
	url(r'^deleteband$',views.deleteBand,name="deleteband"),
	url(r'^displayband$',views.displayBand,name="displayband") 
] 

