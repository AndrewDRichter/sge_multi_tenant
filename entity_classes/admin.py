from django.conf import settings
from django.contrib import admin
from django.db import connection
from .models import EntityClass


def _is_control_tenant():
    return connection.schema_name == getattr(settings, 'CONTROL_TENANT_SCHEMA', 'platform')


def _is_platform_admin(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    grp = getattr(settings, 'PLATFORM_ADMIN_GROUP', None)
    return bool(grp and user.groups.filter(name=grp).exists())


class OnlyControlTenantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def _allowed(self, request):
        return _is_control_tenant() and _is_platform_admin(request.user)

    def has_module_permission(self, request):
        return self._allowed(request)

    def has_view_permission(self, request, obj = ...):
        return self._allowed(request)

    def has_add_permission(self, request):
        return self._allowed(request)

    def has_change_permission(self, request, obj = ...):
        return self._allowed(request)

    def has_delete_permission(self, request, obj = ...):
        return self._allowed(request)


admin.site.register(EntityClass, OnlyControlTenantAdmin)
