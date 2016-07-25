from django.conf.urls import url

from . import views

app_name = 'overtime'

urlpatterns = [
    #/overtime/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/overtime/123/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='report'),
    url(r'report/add/$', views.ReportCreate.as_view(), name='report-add'),
    url(r'report/(?P<pk>[0-9]+)/$', views.ReportUpdate.as_view(), name='report-update'),
    #url(r'report/(?P<pk>[0-9]+)/delete/$', views.ReportDelete.as_view(), name='report-delete'),
    url(r'report/event/add/(?P<report_id>[0-9]+)/$', views.EventCreate.as_view(), name='event-create'),

]

