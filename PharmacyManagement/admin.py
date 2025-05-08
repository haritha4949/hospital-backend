from django.contrib import admin
from .models import Prescriptions,PrescriptionMedicines
# Register your models here.


@admin.register(Prescriptions)
class PrescriptionsAdmin(admin.ModelAdmin):
    list_display = ('prescription_id', 'patient_id', 'doctor_id','tenant_id','visit_id','organization_id', 'follow_up_needed','follow_up_date','test_required','test_details', 'created_at','updated_at') 

@admin.register(PrescriptionMedicines)
class PrescriptionMedicinesAdmin(admin.ModelAdmin):
    list_display = ('medicine_id', 'medicine_name', 'prescription_id', 'dosage', 'frequency', 'duration_days', 'created_at')
