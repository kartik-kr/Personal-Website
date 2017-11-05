"""PersonalWebsite URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
        url(r'^yoda/', admin.site.urls),
        url(r'^blogs/(?P<input_id>[0-9]+)/$', views.Blogs, name='Blogs'),
        url(r'^sentmessage$', views.message, name='message'),
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^.*$', views.Error, name="error"),

]
