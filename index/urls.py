from django.conf.urls import url, include
from . import views
urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
	url(r'^post', include('info.urls')),
]