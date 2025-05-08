from django.db import models
from PatientManagement.models import Patients
from PharmacyManagement.models import Prescriptions,PrescriptionMedicines
# Create your models here.


class MedicationSchedules(models.Model):
    FREQUENCY_CHOICES = [
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('custom', 'Custom'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('stopped', 'Stopped'),
    ]

    schedule_id = models.AutoField(primary_key=True)
    prescription_id = models.ForeignKey(Prescriptions, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(PrescriptionMedicines, on_delete=models.CASCADE)
    dose_count = models.IntegerField()
    dose_taken = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    interval_hours = models.IntegerField(null=True, blank=True)
    days_gap = models.IntegerField(null=True, blank=True)
    preferred_times = models.JSONField()
    timezone = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    next_dose_at = models.DateTimeField()

    def __str__(self):
        return self
