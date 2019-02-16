"""awesome_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from apps.ewallet import views
from apps.user_profile import views as user_profile_views
# mail urls project
# main project url
# 58 apps sabai url yaha rakhda pollutate hunxa
# yesle k garcha
# harek app ko afno url hunxa
# manually create garinxa url.py file in every apps

urlpatterns = [
	path('', views.home, name='home'),
    path('contact', views.contact),
    path('admin/', admin.site.urls),
    path('signup/', user_profile_views.signup),
]

# create app user_profile and function based signup views