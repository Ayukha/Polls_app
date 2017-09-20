from django.conf.urls import url, include

from . import views

app_name = 'polls'
urlpatterns= [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^api/questions/', include("polls.api.urls"), name= 'questions'),
	url(r'^api/choices/', include("polls.api.urls"), name= 'choice'),
]