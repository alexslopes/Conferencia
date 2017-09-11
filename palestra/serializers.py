from .models import *
from rest_framework import serializers


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('acronimos', 'descricao')


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('acronimos', 'descricao')

class ApresentadoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apresentadores
        fields = ('nome', 'filiacao', 'resume')

class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = ('nome', 'capacidade', 'local')

class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atividade
        fields = ('author', 'title', 'abstract', 'tipo', 'tag', 'sala'
, 'data_hora_inicio', 'data_hora_fim', 'apresentadores')
