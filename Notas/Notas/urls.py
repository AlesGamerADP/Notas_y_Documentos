from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, DocumentoViewSet, CarpetaViewSet, EtiquetaViewSet, \
                   NotaUpdateView, DocumentoUpdateView, CarpetaUpdateView, EtiquetaUpdateView, \
                   NotaDeleteView, DocumentoDeleteView, CarpetaDeleteView, EtiquetaDeleteView

router = DefaultRouter()
router.register('notas', NotaViewSet)
router.register('documentos', DocumentoViewSet)
router.register('carpetas', CarpetaViewSet)
router.register('etiquetas', EtiquetaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Las rutas automáticas del router

    # Rutas personalizadas para update y delete
    path('api/notas/update/<int:id>/', NotaUpdateView.as_view(), name='nota_update'),
    path('api/documentos/update/<int:id>/', DocumentoUpdateView.as_view(), name='documento_update'),
    path('api/carpetas/update/<int:id>/', CarpetaUpdateView.as_view(), name='carpeta_update'),
    path('api/etiquetas/update/<int:id>/', EtiquetaUpdateView.as_view(), name='etiqueta_update'),
    
    path('api/notas/delete/<int:id>/', NotaDeleteView.as_view(), name='nota_delete'),
    path('api/documentos/delete/<int:id>/', DocumentoDeleteView.as_view(), name='documento_delete'),
    path('api/carpetas/delete/<int:id>/', CarpetaDeleteView.as_view(), name='carpeta_delete'),
    path('api/etiquetas/delete/<int:id>/', EtiquetaDeleteView.as_view(), name='etiqueta_delete'),
]
