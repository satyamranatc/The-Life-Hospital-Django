from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DieasesSerializer
from .models import Dieases

@api_view(['GET'])
def allDieases(request):
    
    dieases = Dieases.objects.all()
    serializer = DieasesSerializer(dieases, many=True)
    return Response(serializer.data)