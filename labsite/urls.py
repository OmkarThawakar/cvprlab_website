from django.conf.urls import url

from labsite import views



urlpatterns = [
    url(r'^$', views.home , name='index'),
    url(r'^publications/$', views.publications, name='publications'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^members/$', views.peoples, name='members'),
    url(r'^gallery/$', views.gallery, name='gallery'),


    url(r'supervisor/login', views.login_user, name='login_user'),
    url(r'supervisor/dashboard', views.supervisor_dashboard, name='supervisor_dashboard'),
]
