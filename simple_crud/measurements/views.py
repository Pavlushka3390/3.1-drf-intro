from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectSerializers, MeasurementSerializers


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializers
