from django.conf import settings
from django.contrib.auth.models import check_password
from .models import Tailor 

class TailorBackend(object):
    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = Tailor.objects.get(username=username)

            except User.DoesNotExist:
            return None 
        return None

    def get_user(self, user_id):
        try:
            return Tailor.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


