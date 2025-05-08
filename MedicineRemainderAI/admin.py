from django.contrib import admin
from .models import MedicationSchedules


# Register your models here.
@admin.register(MedicationSchedules)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_id','prescription_id', 'patient_id', 'medicine_id','dose_count','dose_taken','start_date','end_date', 
                    'frequency','interval_hours','days_gap','preferred_times','timezone', 
                    'status', 'next_dose_at')