from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login') 
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()

            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('error_page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group:
            return redirect('dashboard')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorised to view this page!')

    return wrapper_function