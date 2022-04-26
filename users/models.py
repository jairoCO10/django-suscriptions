from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager, make_password, Group



Roles =(("admin","admin"), ("creator", "creator"), ("sale", "sale"))

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


# class groups(Group):
#     namegroup = models.CharField(Roles,max_length=250, unique=True)
#     def __str__(self):
#         return self.namegroup
    

class User(AbstractUser):
    pass
    username = None
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    #idgroup = models.ForeignKey(groups,blank=True, null=True, editable=True, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()




# {
#     "is_staff": true,
#     "is_active": true,
#     "email": "andreagomes06@gmail.com",
#     "first_name": "andrea",
#     "last_name": "gomez",
#     "password": "792b3b58"
    
# }

