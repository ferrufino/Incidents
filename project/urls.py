from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^manager/', views.manager),
    url(r'^employee/(?P<empid>\d+)', views.employee, name='employee'),
)
