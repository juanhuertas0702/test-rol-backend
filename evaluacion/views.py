from rest_framework import generics
from .models import Postulante
from .serializers import PostulanteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

# CreateAPIView automáticamente maneja las peticiones POST para crear registros
class RegistroPostulanteView(generics.CreateAPIView):
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer

class LoginView(APIView):
    def post(self, request):
        nombre = request.data.get('nombre')
        contrasena = request.data.get('contrasena')

        try:
            # Buscamos al postulante por su nombre
            postulante = Postulante.objects.get(nombre_completo=nombre)
            
            # Comparamos la contraseña encriptada
            if check_password(contrasena, postulante.contrasena):
                return Response({
                    "mensaje": "Login exitoso", 
                    "postulante_id": postulante.id,
                    "nombre": postulante.nombre_completo
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
                
        except Postulante.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)