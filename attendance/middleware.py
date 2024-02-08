# middleware.py

from django.shortcuts import redirect

class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                # Redirect to the admin panel for superusers
                return redirect('admin:index')
            else:
                # Redirect to the home page for non-superusers
                return redirect('dashboard')  # Change 'home' to your actual home URL

        response = self.get_response(request)
        return response