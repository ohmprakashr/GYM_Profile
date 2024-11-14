from rest_framework import viewsets
from .serializers import gymfieldserializer
from .models import gymfield
class gymfieldviewset(viewsets.ModelViewSet):
	queryset=gymfield.objects.all()
	serializer_class=gymfieldserializer