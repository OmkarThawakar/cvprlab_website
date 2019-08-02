from django.conf.urls import url
from django.contrib.auth.views import  (LoginView,LogoutView)

from labsite import views



urlpatterns = [
    url(r'^$', views.home , name='index'),
    #labsite/register
    url(r'^register/$', views.register, name='register'),
    #labsite/login
    url(r'^login/$',LoginView.as_view(template_name='labsite/forms/login.html'), name='login'),
    #labsite/logout
    url(r'^logout/$',LogoutView.as_view(template_name='labsite/forms/logout.html'), name='logout'),
    #create_profile
    # url(r'^edit_profile/$', views.edit_profile)
    url(r'^create_profile/$', views.CreateProfileFormView.as_view(), name='create_profile'),

    #create_blog profile
    url(r'^create_blog/$', views.CreateBlogFormView.as_view(), name='create_blog'),

    url(r'^(?P<user_id>[0-9]+)/my_blog/$', views.MyBlog, name='my_blog'),
    url(r'^publications/$', views.publications, name='publications'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^members/$', views.peoples, name='members'),
    url(r'^gallery/$', views.gallery, name='gallery'),


    url(r'supervisor/login', views.login_user, name='login_user'),
    url(r'supervisor/dashboard', views.supervisor_dashboard, name='supervisor_dashboard'),
]
