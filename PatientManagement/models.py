from django.db import models
from UserRoleManagement.models import Organizations, Users,Tenant

# Create your models here.
class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    
    # Foreign keys from UserRoleManagement app
    tenant_id = models.ForeignKey(
        'UserRoleManagement.Tenant',
        on_delete=models.CASCADE,
        db_column='tenant_id'
    )
    organization_id = models.ForeignKey(
        'UserRoleManagement.Organizations',
        on_delete=models.CASCADE,
        db_column='organization_id'
    )
    
    # Patient details
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self


class PatientVitals(models.Model):
    vital_id = models.AutoField(primary_key=True)
    
    patient = models.ForeignKey(
        'PatientManagement.Patients',
        on_delete=models.CASCADE,
        db_column='patient_id'
    )
    organization = models.ForeignKey(
        'UserRoleManagement.Organizations',
        on_delete=models.CASCADE,
        db_column='organization_id'
    )
    
    logged_at = models.DateTimeField()
    
    # Vitals
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    respiratory_rate = models.IntegerField()
    oxygen_saturation = models.DecimalField(max_digits=4, decimal_places=1)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vitals for {self.patient} at {self.logged_at}"
    


class PatientAllergies(models.Model):
    allergy_id = models.AutoField(primary_key=True)

    patient_id = models.ForeignKey(
        'PatientManagement.Patients',
        on_delete=models.CASCADE,
        db_column='patient_id'
    )

    allergy_name = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
    reaction = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.allergy_name} ({self.severity}) - {self.patient}"
    
class PatientHistory(models.Model):
    history_id = models.AutoField(primary_key=True)

    # Foreign keys
    tenant_id = models.ForeignKey(
        'UserRoleManagement.Tenant',
        on_delete=models.CASCADE,
        db_column='tenant_id'
    )
    patient_id = models.ForeignKey(
        'PatientManagement.Patients',
        on_delete=models.CASCADE,
        db_column='patient_id'
    )
    organization_id = models.ForeignKey(
        'UserRoleManagement.Organizations',
        on_delete=models.CASCADE,
        db_column='organization_id'
    )
    doctor_id = models.ForeignKey(
        'UserRoleManagement.Users',
        on_delete=models.SET_NULL,
        null=True,
        db_column='doctor_id'
    )

    # Medical history details
    visit_date = models.DateTimeField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True)
    follow_up_date = models.DateField(null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PatientDocuments(models.Model):
    document_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    visit_id = models.ForeignKey(PatientHistory, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    uploaded_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)





    def __str__(self):
        return self