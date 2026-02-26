from rest_framework import generics
from .models import Postulante, ResultadoTest
from .serializers import PostulanteSerializer, ResultadoTestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

class LoginView(APIView):
    def post(self, request):
        nombre = request.data.get('nombre')
        es_admin = request.data.get('es_admin', False)
        
        try:
            if es_admin:
                # Login para admin: nombre + contraseña
                contrasena = request.data.get('contrasena')
                postulante = Postulante.objects.get(nombre_completo=nombre, es_admin=True)
                
                # Verificar contraseña
                if not check_password(contrasena, postulante.contrasena):
                    return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                # Login para usuario normal: nombre + ID usuario
                id_usuario = request.data.get('id_usuario')
                postulante = Postulante.objects.get(nombre_completo=nombre, id_usuario=id_usuario, es_admin=False)
            
            return Response({
                "mensaje": "Login exitoso", 
                "postulante_id": postulante.id,
                "nombre": postulante.nombre_completo,
                "id_usuario": postulante.id_usuario,
                "es_admin": postulante.es_admin
            }, status=status.HTTP_200_OK)
                
        except Postulante.DoesNotExist:
            return Response({"error": "Usuario o credenciales incorrecto"}, status=status.HTTP_401_UNAUTHORIZED)

class AdminView(APIView):
    def get(self, request):
        # Verificar si el usuario es admin
        admin_id = request.headers.get('X-Admin-ID')
        
        try:
            admin = Postulante.objects.get(es_admin=True, id=admin_id)
        except Postulante.DoesNotExist:
            return Response({"error": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)
        
        # Obtener todos los resultados de tests
        resultados = ResultadoTest.objects.select_related('postulante').all()
        serializer = ResultadoTestSerializer(resultados, many=True)
        
        return Response({
            "success": True,
            "resultados": serializer.data
        }, status=status.HTTP_200_OK)