from django.conf import settings
from django.db import connection
from django.http import Http404

class AdminLockdownMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.path.startswith("/admin") and connection.schema_name != getattr(settings, "CONTROL_TENANT_SCHEMA", "platform"):
            raise Http404()
        return self.get_response(request)
