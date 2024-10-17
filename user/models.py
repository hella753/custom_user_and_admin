import datetime
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("Required Field Email is not set")
        if not password:
            raise ValueError("Required Field Password is not set")
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        # პაროლის ჰეშირებისთვის
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        if not email:
            raise ValueError("Required Field Email is not set")
        if not password:
            raise ValueError("Required Field Password is not set")
        # ვიძახებთ create_user-ს რომელიც აბრუნებს შექმნილ იუზერს
        user = self.create_user(email, password, **other_fields)
        # ვხდით ამ ველებს True-ს რადგან მიენიჭოს სუპერმომხმარებლის სტატუსი
        user.is_staff = True
        user.is_superuser = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    # ვალიდატორი აქვს ჯანგოს იუზერს და ბარემ აქაც იყოს.
    username_validator = UnicodeUsernameValidator()
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField("email address", max_length=50, unique=True)
    username = models.CharField(
        "username",
        max_length=20,
        unique=True,
        help_text="Required. 20 characters or fewer",
        validators = [username_validator],
        error_messages = {
            "unique": "A user with that username already exists."
        }
    )

    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    # ჩვენი იუზერ მენეჯერი გამოიყენოს
    objects = UserManager()

    # იუზერნეიმ ფილდად გამოვიყენებთ იმეილს და არა იუზერნეიმს შესვლისთვის.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username}"