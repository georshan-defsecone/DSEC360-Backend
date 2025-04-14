from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)  # Save to the correct database
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    
class Project(models.Model):
    project_id = models.CharField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_author = models.CharField(max_length=255)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name


class Scan(models.Model):
    scan_id = models.CharField(primary_key=True, max_length=100)
    scan_name = models.CharField(max_length=255)
    scan_author = models.CharField(max_length=255)
    scan_status = models.CharField(max_length=50)
    trash = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.scan_name

