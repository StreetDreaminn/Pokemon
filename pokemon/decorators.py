from django.http import HttpResponseForbidden
from .models import *

def get_user_role(user):
    user_role= UserRole.objects.get(user=User.objects.get(username=user))
    return user_role.role

def has_permission(perm_name):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            user_role = get_user_role(request.user)
            if user_role and user_role.permissions.filter(name=perm_name).exists():
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You don't have permission to access this page.")
        return wrapped_view
    return decorator
