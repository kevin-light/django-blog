"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from posts import views as post_views

from posts import urls as posts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', post_views.Index_test01),

    url(r'^posts/', include(posts_urls,namespace='post')), #namespace 区分不用的app，因为不同的app下面可能存在同名的 url
]
