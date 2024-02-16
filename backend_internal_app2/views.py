from datetime import datetime, date
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Qualities, User

@login_required
def user_qualities(request):
    current_user = request.user

    # Filter non-superusers and active users
    all_users = User.objects.filter( is_superuser=False, is_active=True)

    if request.method == 'GET':
        user_id = request.GET.get('userFilter', current_user.id)
        selected_user = get_object_or_404(User, id=user_id)

        if 'dateFilter' in request.GET:
            selected_date = request.GET['dateFilter']
            try:
                selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
                user_qualities = Qualities.objects.filter(user=selected_user, create_date__date=selected_date).first()
            except ValueError:
                user_qualities = None
        else:
            # If dateFilter not present, use today's date
            selected_date = date.today()
            user_qualities = Qualities.objects.filter(user=selected_user, create_date__date=selected_date).first()
    else:
        # If it's not a GET request, use today's date for the current user
        selected_date = date.today()
        user_qualities = Qualities.objects.filter(user=current_user, create_date__date=selected_date).first()

    return render(request, 'dashboard.html', {'user_qualities': user_qualities, 'all_users': all_users})
