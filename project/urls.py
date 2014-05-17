from django.conf.urls import patterns, url
from project import views
from project.views import RegisterTicket


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^manager/', views.manager),
    url(r'^employee/(?P<empid>\d+)', views.employee, name='employee'),
    url(r'^registerTicket/', RegisterTicket.as_view(), name='RegisterTicket'),
    url(r'^allTickets/', views.allTickets)

)
