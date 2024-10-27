"""
URL configuration for ofc_emp_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from application1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',employee,name='employee'),
    path('all_emp/',all_emp,name='all_emp'),
    path('add_emp/',add_emp,name='add_emp'),
    path('remove_emp/<int:id>',remove_emp,name='remove_emp'),
    path('remove_emp/',remove_emp,name='remove_emp'),
    path('filter_emp/',filter_emp,name='filter_emp'),
    path('departments/',departments,name='departments'),
    path('all_dept',all_dept,name='all_dept'),
    path('add_dept',add_dept,name='add_dept'),
    path('remove_dept/<int:id>',remove_dept,name='remove_dept'),
    path('remove_dept/',remove_dept,name='remove_dept'),



]
