from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, pesel, password=None, is_active=True, is_staff=False, is_admin=False,
                    is_student=True):
        if not email:
            raise ValueError("Wpisz poprawny email")
        if not password:
            raise ValueError("Wpisz hasło")
        user = self.model(
            email=email,
            name=name,
            surname=surname,
            pesel=pesel,
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.student = is_student
        user.save(using=self._db)
        return user

    def create_firma(self, email, nazwafirmy, password=None, is_active=True, is_staff=False, is_admin=False,
                     is_firma=True):
        if not email:
            raise ValueError('Wpisz poprawny email')
        if not password:
            raise ValueError('Wpisz haslo')
        user = self.model(
            email=email,
            nazwafirmy=nazwafirmy,
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.firma = is_firma
        user.active = is_active
        user.save(using=self._db)

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            name=None,
            surname=None,
            pesel=None,

        )
        return user


class User(AbstractBaseUser):
    nrindeks = models.CharField(unique=True, null=True, blank=True, max_length=6)
    nazwafirmy = models.CharField(unique=True, null=True, blank=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    pesel = models.CharField(blank=True, null=True, max_length=9)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    firma = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
