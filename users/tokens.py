from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserVerifyToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return user.pk + timestamp + user.is_active

user_verify_token = UserVerifyToken()
