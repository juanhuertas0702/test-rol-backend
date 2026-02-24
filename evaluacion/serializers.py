from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Postulante

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = '__all__'
        # Esto evita que la contraseña se envíe de vuelta por seguridad
        extra_kwargs = {'contrasena': {'write_only': True}} 

    # Esta función encripta la contraseña justo antes de guardarla
    def create(self, validated_data):
        validated_data['contrasena'] = make_password(validated_data.get('contrasena'))
        return super().create(validated_data)