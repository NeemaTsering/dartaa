from django.conf.urls import url 
from . import views
urlpatterns=[
	url(r'^$', views.articles, name='articles'),
	url(r'/new/$', views.new_news, name='new_news'),
]