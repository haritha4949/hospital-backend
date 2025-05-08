from django.contrib import admin
from .models import Patients,PatientVitals,PatientAllergies,PatientHistory,PatientDocuments

# Register your models here.
@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = (
        'patient_id', 'first_name', 'last_name', 'tenant_id', 'organization_id',
        'gender', 'date_of_birth', 'contact_number', 'email','address', 'created_at','updated_at'
    )

@admin.register(PatientVitals)
class PatientVitalsAdmin(admin.ModelAdmin):
    list_display = (
        'vital_id', 'patient_id', 'organization_id', 'logged_at', 
        'blood_pressure', 'heart_rate', 'temperature',
        'respiratory_rate', 'oxygen_saturation', 'weight', 'height','notes', 'created_at'
    )

@admin.register(PatientAllergies)
class PatientAllergiesAdmin(admin.ModelAdmin):
    list_display = (
        'allergy_id', 'patient_id', 'allergy_name',
        'severity', 'reaction', 'notes','created_at'
    )


@admin.register(PatientHistory)
class PatientHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'history_id','patient_id', 'doctor_id', 'organization_id', 'tenant_id',
        'visit_date','diagnosis','treatment','notes', 'follow_up_date', 'created_at', 'updated_at'
    )

@admin.register(PatientDocuments)
class PatientDocumentsAdmin(admin.ModelAdmin):
    list_display = ('document_id', 'patient_id','organization_id','visit_id','file_name','file_path', 'document_type', 'uploaded_by', 'uploaded_at','notes')

