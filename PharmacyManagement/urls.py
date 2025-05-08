from django.urls import path
from .views import PrescriptionsAPI,PrescriptionMedicinesAPI

urlpatterns = [
    path('prescriptions/', PrescriptionsAPI.as_view(), name='prescriptions-api'),
    path('prescription-medicines/', PrescriptionMedicinesAPI.as_view(), name='prescription-medicines-api'),
]
