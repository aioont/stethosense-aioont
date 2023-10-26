# autho/backends.py

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import LabUser

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import LabUser

class LabUserBackend(ModelBackend):
    def authenticate(request, lab_email=None, lab_password=None, **kwargs):
        #User = get_user_model()

        try:
            # Check if a LabUser with the provided lab_email exists
            user = LabUser.objects.get(lab_email=lab_email)

            # Check if the user's lab_password matches
            if user.check_password(lab_password):
                return user
        except LabUser.DoesNotExist:
            # No user with the provided lab_email
            return None

    def get_user(self, user_id):
        #User = get_user_model()
        try:
            return LabUser.objects.get(pk=user_id)
        except LabUser.DoesNotExist:
            return None

