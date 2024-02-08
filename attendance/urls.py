from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('employee',views.course,name='course-page'),
    path('logout',views.logoutuser,name='logout'),
    path(r'manage_employee/<int:pk>',views.manage_course,name='edit-course-modal'),
    path('save_employee',views.save_course,name='save-course'),
    path('delete_employee',views.delete_course,name='delete-course'),
    path('manage_course',views.manage_course,name='manage-course-modal'),

]
