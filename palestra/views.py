from .models import *
from rest_framework import viewsets
from palestra.serializers import *


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TagsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class ApresentadoresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apresentadores.objects.all()
    serializer_class = ApresentadoresSerializer

class SalaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
