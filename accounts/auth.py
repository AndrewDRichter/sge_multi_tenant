from django.db import connection
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication


class TenantAwareJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        token = super().get_validated_token(raw_token)
        token_tenant = token.get('tenant')
        if not token_tenant or token_tenant != connection.schema_name:
            raise AuthenticationFailed('Invalid Tenant Token', code='invalid tenant')
        return token
