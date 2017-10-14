from django.conf.urls import url,include
from . import views

urlpatterns = [
	
	url(r'^$',views.home,name="home"),
	url(r'^addband/$',views.addBand,name="addband"),
	url(r'^success$',views.success,name="success"),
	url(r'^displayband/$',views.displayband,name="displayband"),
	url(r'^displayshows/(?P<pk>\d+)$',views.displayshows,name="displayshows"),	
	url(r'^calendar',views.calandar,name="calendar"),
	url(r'^deleteband/(?P<pk>\d+)$',views.deleteband,name="deleteband"),
	url(r'^deleteshow/(?P<pk>\d+)$',views.deleteshow,name="deleteshow"),
	url(r'^editband/(?P<pk>\d+)$',views.editband,name="editband"),
	url(r'^editshow/(?P<pk>\d+)$',views.editshow,name="editshow"),
	url(r'^addshow/$',views.addshow,name="addshow"),
] 

