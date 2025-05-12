from django.shortcuts import render

# Create your views here.
# PatientManagement/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from .models import Patients,PatientHistory
from .serializers import PatientHistoryUpdateSerializer,PatientsSerializer,PatientVitalsSerializer,PatientAllergiesSerializer,PatientHistorySerializer,PatientDocumentsSerializer,PatientDetailsSerializer,PatientListSerializer

class PatientsAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientVitalsAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PatientVitalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vitals recorded successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientAllergiesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PatientAllergiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Allergy record created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print("Received data:", request.data)  # Debug print
        serializer = PatientHistorySerializer(data=request.data)
        if serializer.is_valid():
            #print("this is error",serializer.validated_data)
            serializer.save()
            return Response({"message": "Patient history created", "data": serializer.data}, status=status.HTTP_201_CREATED)
            print("Errors:", serializer.errors)  # Debugging statement
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDocumentsAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PatientDocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Document uploaded", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
         # Print the entire query_params dictionary to check if parameters exist
        print(f"Request query_params: {request.query_params}")

         # Extracting query parameters
        patient_id = request.query_params.get('patient_id')
        tenant_id = request.query_params.get('tenant_id')
        organization_id = request.query_params.get('organization_id')
        doctor_id = request.query_params.get('doctor_id')


        # patient_id = request.data.get('patient_id')
        # tenant_id = request.data.get('tenant_id')
        # organization_id = request.data.get('organization_id')
        # doctor_id = request.data.get('doctor_id')
        print(f"Received parameters - patient_id: {patient_id}, tenant_id: {tenant_id}, organization_id: {organization_id}, doctor_id: {doctor_id}")

        if not all([patient_id, tenant_id, organization_id, doctor_id]):
            return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patients.objects.filter(
                 patient_id=patient_id,
                 tenant_id_id=tenant_id,
                 organization_id_id=organization_id
            ).first()
        except Patients.DoesNotExist:
            return Response({'error': 'Patient not found. Check IDs.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientDetailsSerializer(
            patient,
            context={
                'tenant_id': tenant_id,
                'organization_id': organization_id,
                'doctor_id': doctor_id
            }
        )
        return Response(serializer.data)
    

# class PatientListAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         doctor_id = request.GET.get('doctor_id')
#         tenant_id = request.GET.get('tenant_id')
#         organization_id = request.GET.get('organization_id')

#         if not (doctor_id and tenant_id and organization_id):
#             return Response({"error": "doctor_id, tenant_id, and organization_id are required."}, status=status.HTTP_400_BAD_REQUEST)

#         # Get patient IDs treated by the doctor
#         patient_ids = PatientHistory.objects.filter(
#             doctor_id=doctor_id,
#             tenant_id=tenant_id,
#             organization_id=organization_id
#         ).values_list('patient_id', flat=True).distinct()

#         # Fetch patient details
#         patients = Patients.objects.filter(
#             patient_id__in=patient_ids,
#             tenant_id=tenant_id,
#             organization_id=organization_id
#         )

#         serializer = PatientListSerializer(patients, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class PatientListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant_id = request.GET.get('tenant_id')
        organization_id = request.GET.get('organization_id')

        if not tenant_id or not organization_id:
            return Response(
                {"error": "tenant_id and organization_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch patient details directly from Patients model
        patients = Patients.objects.filter(
            tenant_id=tenant_id,
            organization_id=organization_id
        )

        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





class PatientHistoryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistoryUpdateSerializer
    lookup_field = 'history_id'
