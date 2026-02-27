from rest_framework import serializers
from .models import Postulante, ResultadoTest

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = ['id', 'nombre_completo', 'id_usuario', 'es_admin', 'fecha_registro']

class ResultadoTestSerializer(serializers.ModelSerializer):
    postulante_nombre = serializers.CharField(source='postulante.nombre_completo', read_only=True)
    
    class Meta:
        model = ResultadoTest
        fields = ['id', 'postulante', 'postulante_nombre', 'rol_principal', 'puntaje_total', 
                  'respuestas_detalle', 'scores', 'fecha_prueba']