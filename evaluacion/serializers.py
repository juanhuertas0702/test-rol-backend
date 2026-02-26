from rest_framework import serializers
from .models import Postulante, ResultadoTest

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = ['id', 'nombre_completo', 'id_usuario', 'es_admin', 'fecha_registro']

class ResultadoTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoTest
        fields = ['id', 'postulante', 'puntaje_total', 'respuestas_detalle', 'fecha_prueba']