from django.contrib import admin

# Register your models here.

from .models import DoctorSchedule,Appointment

@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'schedule_id', 'doctor_id', 'day_of_week', 'available_from',
        'available_to','break_start','break_end', 'consultation_duration', 'appointment_gap',
        'created_at','updated_at'
    )
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'appointment_id', 'appointment_date', 'slot_start', 'slot_end',
        'doctor_id', 'patient_id','schedule_id', 'consultation_type', 'status', 'booking_method',
        'notes','created_at','updated_at'

    )