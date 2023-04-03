"""capstone URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from website.views import welcome, date, about
from planner.views import manager_detail, team_detail, location_detail, manager_list, location_list, member_detail
from planner.views import new_member, update_member, delete_member, new_location, update_location, delete_location
from planner.views import new_manager, update_manager, delete_manager, new_team, update_team, delete_team
from planner.views import create_member, create_admin, login_view, logout_view, admin_group
from planner.views import user_group, access_denied


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('date', date),
    path('about', about),
    path('manager/<int:id>/', manager_detail, name='manager_detail'),
    path('member/<int:id>/', member_detail, name='member'),
    path('team/<int:id>/', team_detail, name='team'),
    path('location/<int:id>.html', location_detail, name='location_detail'),
    path('manager', manager_list, name="manager"),
    path('location/', location_list, name="location"),
    path('new_member', new_member, name="new_member"),
    path('update-member/<int:member_id>/', update_member, name='update_member'),
    path('delete-member/<int:member_id>/', delete_member, name='delete_member'),
    path('new_manager', new_manager, name="new_manager"),
    path('update-manager/<int:manager_id>/', update_manager, name='update_manager'),
    path('delete-manager/<int:manager_id>/', delete_manager, name="delete_manager"),
    path('new_location', new_location, name="new_location"),
    path('update-location/<int:location_id>/', update_location, name='update_location'),
    path('delete-location/<int:location_id>/', delete_location, name='delete_location'),
    path('new_team', new_team, name="new_team"),
    path('update-team/<int:team_id>/', update_team, name='update_team'),
    path('delete-team/<int:team_id>/', delete_team, name='delete_team'),
    path('create-member/', create_member, name='create_member'),
    path('create-admin/', create_admin, name='create_admin'),
    path('login/login.html', login_view, name='login'),
    path('login/access_denied.html', access_denied, name='access_denied'),
    path('login/login.html', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_group/', admin_group, name='admin_group'),
    path('user_group/', user_group, name='user_group'),
]