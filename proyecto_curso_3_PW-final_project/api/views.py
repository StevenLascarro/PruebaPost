from .models import Carro
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import CarroSerializer

#Conjunto de vistas para el CRUD del modelo ejemplo
class CarroViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint para el modelo carro, admite
    GET,POST, PUT, PATCH, DELETE
    """
    queryset = Carro.objects.all().order_by('-fecha_creacion')
    serializer_class = CarroSerializer
