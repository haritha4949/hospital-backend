from django.db import models
from UserRoleManagement.models import Organizations, Users,Tenant
from PatientManagement.models import Patients,PatientHistory
# Create your models here.

class Prescriptions(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='prescribed_by')
    visit_id = models.ForeignKey(PatientHistory, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)

    follow_up_needed = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)

    test_required = models.BooleanField(default=False)
    test_details = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PrescriptionMedicines(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    prescription_id = models.ForeignKey(Prescriptions, on_delete=models.CASCADE, related_name='medicines')
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration_days = models.IntegerField()
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"History for {self.patient} on {self.visit_date.date()}"