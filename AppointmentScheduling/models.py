from django.db import models

# Create your models here.
from django.db import models
from UserRoleManagement.models import Users,Tenant
from PatientManagement.models import Patients

class DoctorSchedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    schedule_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    available_from = models.TimeField()
    available_to = models.TimeField()
    break_start = models.TimeField()
    break_end = models.TimeField()
    consultation_duration = models.IntegerField()
    appointment_gap = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('doctor_id', 'day_of_week')

    def __str__(self):
        return self
class Appointment(models.Model):
    CONSULTATION_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    BOOKING_METHOD_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    appointment_id = models.AutoField(primary_key=True)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    slot_start = models.TimeField()
    slot_end = models.TimeField()
    consultation_type = models.CharField(max_length=10, choices=CONSULTATION_CHOICES)
    status = models.CharField(max_length=50)
    booking_method = models.CharField(max_length=10, choices=BOOKING_METHOD_CHOICES)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self