from django.conf.urls import patterns, url
from project import views
from project.views import RegisterTicket, Manager


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^manager/', Manager.as_view(), name='Manager'),
    url(r'^employee/', views.employee),
    url(r'^registerTicket/', RegisterTicket.as_view(), name='RegisterTicket'),
    url(r'^allTickets/', views.allTickets)

)
