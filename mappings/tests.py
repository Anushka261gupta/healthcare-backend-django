from django.test import TestCase

# Create your tests here.
from rest_framework import generics, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingCreateView(generics.CreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(assigned_by=self.request.user)


class MappingListView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()


class MappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)


class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()