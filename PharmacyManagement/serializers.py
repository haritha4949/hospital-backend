from rest_framework import serializers
from .models import Prescriptions,PrescriptionMedicines

class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = '__all__'

class PrescriptionMedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedicines
        fields = '__all__'