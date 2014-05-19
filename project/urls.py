from django.conf.urls import patterns, url
from project import views
from project.views import RegisterTicket, ManagerView, AssignEmployee, EmployeeView


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^manager/(?P<adminid>\d+)', ManagerView.as_view(), name='Manager'),
    url(r'^employee/(?P<empid>\d+)', EmployeeView.as_view(), name='employee'),
    url(r'^registerTicket/(?P<adminid>\d)', RegisterTicket.as_view(), name='RegisterTicket'),
    url(r'^AssignEmployee/(?P<adminid>\d)', AssignEmployee.as_view(), name='AssignEmployee'),
    url(r'^CloseIncident/(?P<adminid>\d)', RegisterTicket.as_view(), name='CloseIncident'),
    url(r'^allTickets/', views.allTickets)


)
