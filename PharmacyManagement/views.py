from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PrescriptionsSerializer,PrescriptionMedicinesSerializer

class PrescriptionsAPI(APIView):
    def post(self, request):
        serializer = PrescriptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Prescription added", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionMedicinesAPI(APIView):
    def post(self, request):
        serializer = PrescriptionMedicinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Prescription medicine  added", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)