from rest_framework import serializers
from .models import Business, Dependence, BusinessDependence

class DependenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependence
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    # Aquí anidamos el serializador de Dependence para obtener información completa
    dependences = DependenceSerializer(many=True, read_only=True)
    class Meta:
        model = Business
        fields = ['id', 'code', 'name', 'created_at', 'updated_at', 'dependences']  # Ordenamos los campos

class BusinessDependenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDependence
        fields = '__all__'