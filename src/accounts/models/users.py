import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone

from src.accounts.managers import UserManager


# from src.accounts.managers import UserManager
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField("first name", max_length=100, blank=True)
    mid_name = models.CharField("middle name", max_length=50, null=True, blank=True)
    last_name = models.CharField("last name", max_length=100, blank=True)
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s %s %s" %(self.first_name, self.mid_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
