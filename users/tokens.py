from django.contrib.auth.tokens import PasswordResetTokenGenerator


# 유저 토큰 정보에 pk, 시간, active 여부를 함께 담아 넘겨줄 수 있게 함
class UserVerifyToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return user.pk + timestamp + user.is_active


user_verify_token = UserVerifyToken()
