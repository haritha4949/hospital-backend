# PatientManagement/urls.py
from django.urls import path
from .views import PatientsAPI,PatientVitalsAPI,PatientAllergiesAPI,PatientHistoryAPI,PatientDocumentsAPI,PatientDetailAPIView,PatientListAPI

urlpatterns = [
    path('patients/', PatientsAPI.as_view(), name='patients-create'),
    path('vitals/', PatientVitalsAPI.as_view(), name='patient-vitals-create'),
    path('allergies/', PatientAllergiesAPI.as_view(), name='allergies-api'),
    path('history/', PatientHistoryAPI.as_view(), name='patient-history-api'),
    path('documents/', PatientDocumentsAPI.as_view(), name='patient-documents-api'),
    path('patient-details/', PatientDetailAPIView.as_view(), name='patient-details'),
    path('patientsList/', PatientListAPI.as_view(), name='patient-list'),
]
