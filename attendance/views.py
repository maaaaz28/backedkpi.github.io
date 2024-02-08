from unicodedata import category
from aiohttp import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
# from ams.settings import MEDIA_ROOT, MEDIA_URL
from attendance.models import Course, Department

from attendance.forms import  SaveCourse

deparment_list = Department.objects.exclude(status = 2).all()
context = {
    'page_title' : 'Simple Blog Site',
    'deparment_list' : deparment_list,
    'deparment_list_limited' : deparment_list[:3]
}
#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')


#EMPLOYEE
@login_required
def course(request):
    courses = Course.objects.all()
    context['page_title'] = "BACKEND INTERNAL | ADMIN"
    context['courses'] = courses
    return render(request, 'course_mgt.html',context)

@login_required
def manage_course(request,pk=None):
    # course = course.objects.all()
    if pk == None:
        course = {}
        department = Department.objects.filter(status=1).all()
    elif pk > 0:
        course = Course.objects.filter(id=pk).first()
        department = Department.objects.filter(Q(status=1) or Q(id = course.id)).all()
    else:
        department = Department.objects.filter(status=1).all()
        course = {}
    context['page_title'] = "Manage Course"
    context['departments'] = department
    context['course'] = course

    return render(request, 'manage_course.html',context)

@login_required
def save_course(request):
    resp = { 'status':'failed' , 'msg' : '' }
    if request.method == 'POST':
        course = None
        print(not request.POST['id'] == '')
        if not request.POST['id'] == '':
            course = Course.objects.filter(id=request.POST['id']).first()
        if not course == None:
            form = SaveCourse(request.POST,instance = course)
        else:
            form = SaveCourse(request.POST)
    if form.is_valid():
        form.save()
        resp['status'] = 'success'
        messages.success(request, 'Course has been saved successfully')
    else:
        for field in form:
            for error in field.errors:
                resp['msg'] += str(error + '<br>')
        if not course == None:
            form = SaveCourse(instance = course)
       
    return HttpResponse(json.dumps(resp),content_type="application/json")

@login_required
def delete_course(request):
    resp={'status' : 'failed', 'msg':''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            course = Course.objects.filter(id = id).first()
            course.delete()
            resp['status'] = 'success'
            messages.success(request,'Course has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp),content_type="application/json")
