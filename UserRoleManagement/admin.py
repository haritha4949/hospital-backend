from django.contrib import admin

# Register your models here.
from .models import License, Tenant,Users,Organizations,UserOrganizations,UserRoles

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license_key', 'license_type', 'status', 'purchase_date', 'expiry_date')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_name', 'license_id', 'created_at', 'updated_at')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'first_name', 'last_name', 'tenant', 'phone_number', 'created_at', 'updated_at')

@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = (
        'organization_id',
        'org_name',
        'org_type',
        'tenant',
        'address',
        'contact_info',
        'created_at',
        'updated_at',
    )

@admin.register(UserRoles)
class UserRolesAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name', 'role_type', 'tenant_id', 'created_at', 'updated_at')

@admin.register(UserOrganizations)
class UserOrganizationsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'organization_id', 'role_id', 'is_primary', 'created_at')

