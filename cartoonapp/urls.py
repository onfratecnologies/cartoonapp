"""cartoonapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import include, re_path, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from rest_framework import routers
from apiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/post-image', views.postImage),
    re_path(r'^api/get-image/(?P<pk>[A-Z]+[0-9]+)$', views.getImageFaces),
    #re_path(r'^api/get-image/<pk>', views.getImageFaces),
    #re_path(r'^api/get-image/<str:ordering>', views.getImageFaces),
    ###############################################################################
    # re_path(r'^posts/(?P<ordering>top|new)/$', posts, name='posts')
    # re_path(r'^api/x-image/(?P<pk>[0-9]+)$', views.getImageFaces),
    # re_path(r'^(?P<slug>[-\w\d]+)-(?P<post_id>\d+)/$', views.index, name='post'),
    # path('posts/<slug:slug>/', views.index, name='unique_slug'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
