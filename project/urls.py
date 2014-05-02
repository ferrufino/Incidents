from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<adminid>\d+)/manager/', views.manager, name='manager'),
    url(r'^(?P<empid>\d+)/employee/', views.employee, name='employee'),
)
