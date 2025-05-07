from django.db import models

# Modelo para las Etiquetas
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para las Carpetas
class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Modelo para las Notas
class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='notas')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.titulo

# Modelo para los Documentos
class Documento(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='documentos')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.titulo
