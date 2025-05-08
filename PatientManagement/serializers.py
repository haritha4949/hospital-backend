from rest_framework import serializers
from .models import Patients, PatientVitals,PatientAllergies,PatientHistory,PatientDocuments

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class PatientVitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVitals
        fields = '__all__'

class PatientAllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAllergies
        fields = '__all__'

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'

class PatientDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDocuments
        fields = '__all__'

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = [
            'history_id',
            'visit_date',
            'diagnosis',
            'treatment',
            'notes',
            'follow_up_date'
        ]

class PatientDetailsSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Patients
        fields = [
            'patient_id',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'contact_number',
            'email',
            'address',
            'created_at',
            'updated_at',
            'history'
        ]

    def get_history(self, obj):
        tenant_id = self.context.get('tenant_id')
        organization_id = self.context.get('organization_id')
        doctor_id = self.context.get('doctor_id')
        history_qs = PatientHistory.objects.filter(
            patient_id=obj,
            tenant_id=tenant_id,
            organization_id=organization_id,
            doctor_id=doctor_id
        )
        return PatientHistorySerializer(history_qs, many=True).data
    


class PatientListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Patients
        fields = ['patient_id', 'full_name', 'date_of_birth', 'gender', 'contact_number']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

