from unicodedata import category
from aiohttp import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from attendance.forms import CustomUserCreationForm, QForm, QualitiesForm
# from attendance.forms import SaveCourse
# from attendance.models import Course, Department
# from ams.settings import MEDIA_ROOT, MEDIA_URL
# from attendance.models import Department

from backend_internal_app2.models import Qualities
# from attendance.forms import  SaveCourse
from django.contrib.auth import get_user_model

User = get_user_model()

# deparment_list = Department.objects.exclude(status = 2).all()
# context = {
#     'page_title' : 'Simple Blog Site',
#     'deparment_list' : deparment_list,
#     'deparment_list_limited' : deparment_list[:3]
# }
# #Logout
def logoutuser(request):
    logout(request)
    return redirect('/')


#EMPLOYEE
@login_required
def course(request):
    context ={}
    users = User.objects.all()
    print(users)
    
    context['page_title'] = "BACKEND INTERNAL | ADMIN"
    context['users'] = users
    return render(request, 'user_mgt.html',context)

@login_required
def manage(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_mgt')
    else:
        form = CustomUserCreationForm()
        users=User.objects.all()
        context={'form': form, 'users': users}
        return render(request, 'manage_user.html', context )

def dashboard(request):
    courses = User.objects.all()
    return render(request, 'user_mgt.html', {'courses': courses})
    pass

@login_required
def assign_qualities(request):
    if request.method == 'POST':
        form = QualitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('score')  
    else:
        form = QualitiesForm()
        users = User.objects.all()
        context = {'form': form, 'users': users}
        return render(request, 'addscore.html', context)
@login_required
def save_course(request, pk=None):
    pass

@login_required
def delete_course(request, pk=None):
    pass

@login_required
def assign_marks(request, pk=None):
    pass

@login_required
def view_scores_history(request):
    # Your existing view logic here
    
    # Fetch previous and latest users
    previous_users = Qualities.objects.order_by('-create_date').exclude(user=request.user)[:10]
    latest_user = Qualities.objects.filter(user=request.user).order_by('-create_date').first()

    context = {
        'form': QForm,  # Replace with your actual form instance
        'previous_users': previous_users,
        'latest_user': latest_user,
    }

    return render(request, 'score.html', context)

@login_required
def delete_course(request):
    resp={'status' : 'failed', 'msg':''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            course = User.objects.filter(id = id).first()
            course.delete()
            resp['status'] = 'success'
            messages.success(request,'Course has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp),content_type="application/json")

# def assign_marks(request):
#     # Assuming you have a Course model and you want to fetch all courses
#     courses = Course.objects.all()

#     # Retrieve course IDs from the URL
#     course_ids_str = request.GET.get('courses', '')
#     course_ids = list(map(int, course_ids_str.split(',')))

#     return render(request, 'assign-marks.html', {'courses': courses, 'course_ids': course_ids})
