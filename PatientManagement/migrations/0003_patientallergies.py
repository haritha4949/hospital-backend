# Generated by Django 5.2 on 2025-04-16 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientManagement', '0002_patientvitals'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAllergies',
            fields=[
                ('allergy_id', models.AutoField(primary_key=True, serialize=False)),
                ('allergy_name', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=20)),
                ('reaction', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient_id', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, to='PatientManagement.patients')),
            ],
        ),
    ]
