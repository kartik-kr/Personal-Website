"""PersonalWebsite URL Configuration
"""
from django.conf.urls import include,url
from django.contrib import admin
from index import views
urlpatterns = [
        url(r'^yoda/', admin.site.urls),
        url(r'^', include('index.urls')),
    url(r'^.*$', views.Error, name="error"),
]
