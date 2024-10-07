from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from .models import Business, Dependence, BusinessDependence
from .serializers import BusinessSerializer, DependenceSerializer, BusinessDependenceSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    
    @action(detail=True, methods=['get'])
    def dependences(self, request, pk=None):
        """
        Retorna las dependencias asociadas a una empresa específica.
        """
        try:
            # Obtener la empresa por su ID
            business = Business.objects.get(pk=pk)

            # Obtener todas las dependencias asociadas a esta empresa
            dependences = business.dependences.all()

            # Serializar las dependencias
            serializer = DependenceSerializer(dependences, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Business.DoesNotExist:
            return Response({"error": "Empresa no encontrada."}, status=status.HTTP_404_NOT_FOUND)

class DependenceViewSet(viewsets.ModelViewSet):
    queryset = Dependence.objects.all()
    serializer_class = DependenceSerializer

class BusinessDependenceViewSet(viewsets.ModelViewSet):
    queryset = BusinessDependence.objects.all()
    serializer_class = BusinessDependenceSerializer

    @action(detail=True, methods=['post'])
    def sync_dependences(self, request, pk=None):
        """
        Este método permite sincronizar dependencias para una empresa específica.
        Recibe el ID de la empresa y una lista de IDs de dependencias.
        """
        try:
            # Obtener la empresa por el `pk`
            business = Business.objects.get(pk=pk)

            # Obtener la lista de dependencias desde el request
            dependences_ids = request.data.get('dependences', [])

            # Convertir las dependencias a objetos Dependence
            dependences = Dependence.objects.filter(id__in=dependences_ids)

            # Eliminar todas las dependencias existentes y asociar las nuevas
            business.dependences.clear()
            business.dependences.add(*dependences)

            return Response({"message": "Dependencias sincronizadas correctamente."}, status=status.HTTP_200_OK)
        except Business.DoesNotExist:
            return Response({"error": "Empresa no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
