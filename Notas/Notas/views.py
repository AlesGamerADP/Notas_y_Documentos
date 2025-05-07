from rest_framework import viewsets, permissions, generics, filters
from .models import Nota, Documento, Carpeta, Etiqueta
from .serializers import NotaSerializer, DocumentoSerializer, CarpetaSerializer, EtiquetaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NotaSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['id', 'titulo', 'fecha_creacion']  # Ordenar por los campos

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DocumentoSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['id', 'titulo', 'fecha_creacion']

class CarpetaViewSet(viewsets.ModelViewSet):
    queryset = Carpeta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarpetaSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['id', 'nombre']

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EtiquetaSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['id', 'nombre']

class NotaUpdateView(generics.UpdateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    lookup_field = 'id'

class DocumentoUpdateView(generics.UpdateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    lookup_field = 'id'

class CarpetaUpdateView(generics.UpdateAPIView):
    queryset = Carpeta.objects.all()
    serializer_class = CarpetaSerializer
    lookup_field = 'id'

class EtiquetaUpdateView(generics.UpdateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    lookup_field = 'id'

class NotaDeleteView(generics.DestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    lookup_field = 'id'

class DocumentoDeleteView(generics.DestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    lookup_field = 'id'

class CarpetaDeleteView(generics.DestroyAPIView):
    queryset = Carpeta.objects.all()
    serializer_class = CarpetaSerializer
    lookup_field = 'id'

class EtiquetaDeleteView(generics.DestroyAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    lookup_field = 'id'
