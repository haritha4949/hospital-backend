# Generated by Django 5.2 on 2025-04-16 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserRoleManagement', '0005_rename_role_userorganizations_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization_id', models.ForeignKey(db_column='organization_id', on_delete=django.db.models.deletion.CASCADE, to='UserRoleManagement.organizations')),
                ('tenant_id', models.ForeignKey(db_column='tenant_id', on_delete=django.db.models.deletion.CASCADE, to='UserRoleManagement.tenant')),
            ],
        ),
    ]
