from django.db import models

class Postulante(models.Model):
    nombre_completo = models.CharField(max_length=255)
    id_usuario = models.CharField(max_length=50, unique=True, null=True, blank=True)
    contrasena = models.CharField(max_length=128, null=True, blank=True)
    es_admin = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo


class ResultadoTest(models.Model):
    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE, related_name='resultados')
    respuestas_detalle = models.JSONField(default=list, blank=True)
    scores = models.JSONField(default=dict, blank=True)
    rol_principal = models.CharField(max_length=1, default='A')
    puntaje_total = models.IntegerField(default=0)
    fecha_prueba = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_prueba']

    def __str__(self):
        return f"{self.postulante.nombre_completo} - {self.rol_principal}"
