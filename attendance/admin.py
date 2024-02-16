from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import  Course
class MyUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("last_login","date_joined")
# admin.site.register(Course)

