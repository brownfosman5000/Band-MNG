from django.conf.urls import url,include
import views

urlpatters = [
	url(r'^$',include(views.index))
] 

