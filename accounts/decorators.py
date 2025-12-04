from rest_framework.response import Response
from functools import wraps

def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return Response({"error": "Authentication required"}, status=401)

            if user.role not in allowed_roles:
                return Response({"error": "Permission denied"}, status=403)

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
