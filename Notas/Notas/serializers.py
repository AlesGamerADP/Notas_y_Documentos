from rest_framework import serializers
from .models import Nota, Documento, Carpeta, Etiqueta

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'
