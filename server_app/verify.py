from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model

from server_app.models import UserType, XSession

# class CSRFCheck(CsrfViewMiddleware):
#     def _reject(self, request, reason):
#         return reason

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()


        
        authorization_header = request.headers.get("Authorization")
        
        if not authorization_header:
            return None
        
        try:
            authorization=authorization_header.split(" ")

            # if str.upper(authorization[0]) == 'ACCESS':
            #     user = User.objects.get(username='admin')
            #     return (user, None)

            session_id = authorization[1]
            session = XSession.objects.get(session = session_id)

        except XSession.DoesNotExist:
            raise exceptions.AuthenticationFailed("Token does not exist")

        user = session.user_type.user

        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        
        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is not active")

        return (user, None)