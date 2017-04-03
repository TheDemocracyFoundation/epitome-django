from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as _ModelBackend

User = get_user_model()


class EmailOrUsernameModelBackend(_ModelBackend):
    """ Authenticate user by username or email """

	def authenticate(self, username=None, password=None):
		#if '@' in username:
		kwargs = {'email': username}
		#else:
		#	kwargs = {'username': username}
		try:
			user = User.objects.get(**kwargs)
			if user.check_password(password):
				return user
			else:
				return None
		except User.DoesNotExist:
			return None

	def get_user(self, user_id=None):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
