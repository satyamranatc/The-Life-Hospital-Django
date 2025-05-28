from rest_framework.serializers import ModelSerializer
from .models import Dieases

class DieasesSerializer(ModelSerializer):
    class Meta:
        model = Dieases
        fields = "__all__"

        



