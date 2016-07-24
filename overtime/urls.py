from django.conf.urls import url

from . import views

app_name = 'overtime'

urlpatterns = [
    #/overtime/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/overtime/123/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='report'),

    url(r'^report/add/$', views.ReportCreate.as_view(), name='report-add'),
]

