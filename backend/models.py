from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class UserType(models.TextChoices):
    INFLUENCER = "influencer"
    BUSINESS = "business"

    @staticmethod
    def max_length() -> int:
        return 10


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Cate and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    # Global user fields.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        choices=UserType.choices, max_length=UserType.max_length()
    )
    phone = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profile_picture = models.FileField(null=True, blank=True)
    avg_pay = models.FloatField(
        null=True, blank=True
    )  # Looking for pay / Willing to pay.
    country = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)

    # Influencer only fields.
    known_as = models.CharField(max_length=255, null=True, blank=True)
    audience_num = models.IntegerField(null=True, blank=True)
    avg_views = models.IntegerField(null=True, blank=True)

    # Business only fields.
    business_name = models.CharField(max_length=255, null=True, blank=True)
    business_link = models.URLField(null=True, blank=True)

    # Permission fields.
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Platform(models.Model):
    name = models.CharField(max_length=255, unique=True)  # e.g. Youtube

    def __str__(self):
        return self.name


class UserPlatform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.email + ": " + self.platform.name


class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class UserKeyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email + ": " + self.keyword.name
