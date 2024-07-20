from django.contrib.auth.backends import BaseBackend
from .models import registeration

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = registeration.objects.get(username=username, pwd=password)
            return user
        except registeration.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return registeration.objects.get(pk=user_id)
        except registeration.DoesNotExist:
            return None
