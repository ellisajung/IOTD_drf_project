from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일을 입력하세요")
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        # superuser가 이메일 인증 안하게!
        user.is_active = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class FashionChoices(models.TextChoices):
        CASUAL = "CASUAL", "캐쥬얼"
        STREET = "STREET", "스트릿"
        FORMAL = "FORMAL", "포멀"
        RETRO = "RETRO", "레트로"
        ATHLEISURE = "ATHLEISURE", "애슬레저"
        FUNK = "FUNK", "펑크"

    email = models.EmailField("이메일", max_length=255, unique=True)
    nickname = models.CharField("닉네임", max_length=50, default="사용자")
    profile_img = models.ImageField("프로필 이미지", null=True, blank=True, upload_to="%Y/%m")
    fashion = models.CharField(
        "패션", max_length=50, choices=FashionChoices.choices, null=True
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )

    # 팔로잉 수
    def total_followings(self):
        return self.followings.count()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
