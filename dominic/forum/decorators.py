from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:  # Redirect if the user is already register or login
            return redirect('description')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
