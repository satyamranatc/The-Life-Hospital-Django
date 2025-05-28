from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DoctorSerializer
from .models import Doctor

@api_view(['GET'])
def allDoctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)
    