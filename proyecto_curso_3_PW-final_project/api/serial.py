from rest_framework import serializers

#Se importa el modelo
from .models import Carro

#Se crea el serializador
class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ['id','modelo','marca','referencia','fecha_creacion','valor']