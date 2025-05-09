# Generated by Django 5.2 on 2025-04-19 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentScheduling', '0001_initial'),
        ('PatientManagement', '0008_remove_prescriptions_doctor_id_and_more'),
        ('UserRoleManagement', '0005_rename_role_userorganizations_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('slot_start', models.TimeField()),
                ('slot_end', models.TimeField()),
                ('consultation_type', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=10)),
                ('status', models.CharField(max_length=50)),
                ('booking_method', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserRoleManagement.users')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientManagement.patients')),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppointmentScheduling.doctorschedule')),
                ('tenant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserRoleManagement.tenant')),
            ],
        ),
    ]
