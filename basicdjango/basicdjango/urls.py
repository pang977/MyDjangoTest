"""basicdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blogs import views

urlpatterns = [
    path('admin', admin.site.urls),# path คือ / ในเว็บการเข้าถึงแบบไฟล์
    path('',views.hello,name='home'), # ไม่มีแปลว่าหน้าแรก 
    path('page1',views.page1),
    path('MyMaple',views.MyMaple),
    path('page2',views.page2),
    path('addinfinite',views.addinfinite),
    path('form',views.formpage),
    path('addform',views.addform),
    path('loginform',views.loginform),
    path('login',views.login),
    path('logout',views.logout)
]
