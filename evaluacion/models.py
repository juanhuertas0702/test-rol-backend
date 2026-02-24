from django.db import models

class Postulante(models.Model):
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    documento = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=128, default='')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo

class ResultadoTest(models.Model):
    # Conectamos el resultado con el postulante
    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE, related_name='resultados')
    puntaje_total = models.IntegerField()
    
    # Opcional pero muy recomendado: un campo JSON para guardar exactamente qué 
    # respondió en la pregunta 8, la 11, etc.
    respuestas_detalle = models.JSONField(blank=True, null=True) 
    fecha_prueba = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.postulante.nombre_completo} - Puntaje: {self.puntaje_total}"
# Create your models here.
