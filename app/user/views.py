"""
Views for the user API.
"""
from datetime import timezone
from rest_framework.authtoken.models import Token

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import (UserSerializer, AuthTokenSerializer)
from rest_framework.response import Response


class CreateUserView(generics.CreateAPIView):
    """Create new user in the system by api reqoust // this method handle the post request"""
    serializer_class = UserSerializer




# class ExpiringToken(Token):
#     """
#     Subclass of Token model to add an expiration time.
#     """
#
#     # Set the expiration time for tokens in seconds (e.g., 1 hour)
#     EXPIRATION_TIME = 60 * 60
#
#     @property
#     def is_expired(self):
#         """
#         Check if the token is expired.
#         """
#         return self.created < timezone.now() - timezone.timedelta(seconds=self.EXPIRATION_TIME)

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     return Response({
    #         'user_id': user.id,
    #         'email': user.email,
    #         'birthday': user.birthday,
    #         'token': user.auth_token.key,
    #     })


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """to manage data that come from authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
