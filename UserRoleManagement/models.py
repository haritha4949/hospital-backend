from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class License(models.Model):
    license_id = models.AutoField(primary_key=True)
    license_key = models.CharField(max_length=255, unique=True)
    purchase_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    license_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    license_id = models.ForeignKey('UserRoleManagement.License', on_delete=models.CASCADE)
    tenant_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models

# Step 1: Custom manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Step 2: Main user model


class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey('UserRoleManagement.Tenant', on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    @property
    def id(self):
        return self.user_id

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class Users(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     tenant = models.ForeignKey('UserRoleManagement.Tenant', on_delete=models.CASCADE)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)  # You can use Django's hashing system instead of storing raw hash
#     phone_number = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Organizations(models.Model):
    organization_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, db_column='tenant_id')
    org_type = models.CharField(max_length=100)
    org_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserRoles(models.Model):
    ROLE_TYPE_CHOICES = (
        (0, 'Default'),
        (1, 'Custom'),
    )

    role_id = models.AutoField(primary_key=True)
    tenant_id = models.ForeignKey('Tenant', on_delete=models.CASCADE, db_column='tenant_id', null=True, blank=True)
    role_name = models.CharField(max_length=100)
    role_type = models.IntegerField(choices=ROLE_TYPE_CHOICES, default=0)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserOrganizations(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='user_id')
    organization = models.ForeignKey('Organizations', on_delete=models.CASCADE, db_column='organization_id')
    role_id = models.ForeignKey(UserRoles, on_delete=models.SET_NULL, null=True, db_column='role_id')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self
    