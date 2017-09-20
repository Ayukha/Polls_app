from django.conf.urls import url

from polls.api.views import QuestionListAPIView , ChoiceListAPIView

urlpatterns = [
    url(r'^$', QuestionListAPIView.as_view(), name='question'),
    url(r'^show$', ChoiceListAPIView.as_view(), name='choice'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
] 