from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('employee',views.course,name='employee'),
    path('logout',views.logoutuser,name='logout'),
    # path(r'manage_employee/<int:pk>',views.manage_course,name='edit-course-modal'),
    # path('save_employee',views.save_course,name='save-course'),
    path('delete_employee',views.delete_course,name='delete-course'),
    path('manage_course',views.manage,name='manage-course-modal'),
    path('assign_qualities/', views.assign_qualities, name='assign_qualities'),

]
