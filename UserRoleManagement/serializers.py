# UserRoleManagement/serializers.py
from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['tenant', 'email', 'password', 'phone_number', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)








# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['user_id', 'tenant', 'email', 'password', 'phone_number', 'first_name', 'last_name']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super().create(validated_data)