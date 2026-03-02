from rest_framework import generics
from .models import Postulante, ResultadoTest
from .serializers import PostulanteSerializer, ResultadoTestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from collections import Counter

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

class VerifyTestView(APIView):
    """Verificar si el usuario ya respondió el test"""
    def get(self, request):
        postulante_id = request.query_params.get('postulante_id')
        
        try:
            resultado = ResultadoTest.objects.filter(postulante_id=postulante_id).latest('fecha_prueba')
            return Response({
                "ya_respondio": True,
                "fecha_prueba": resultado.fecha_prueba.strftime('%d/%m/%Y %H:%M:%S'),
                "rol_principal": resultado.rol_principal
            }, status=status.HTTP_200_OK)
        except ResultadoTest.DoesNotExist:
            return Response({
                "ya_respondio": False
            }, status=status.HTTP_200_OK)

class GuardarTestView(APIView):
    """Guardar las respuestas del test"""
    def post(self, request):
        try:
            postulante_id = request.data.get('postulante_id')
            respuestas = request.data.get('respuestas', [])
            rol_principal = request.data.get('rol_principal')
            scores = request.data.get('scores', {})
            
            # Validar que tengamos los datos requeridos
            if not postulante_id or not rol_principal:
                return Response(
                    {"error": "postulante_id y rol_principal son requeridos"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Calcular puntaje total
            puntaje_total = sum(scores.values()) if scores else 0
            
            # Buscar el postulante
            postulante = Postulante.objects.get(id=postulante_id)
            
            # Crear el registro de resultado
            resultado = ResultadoTest.objects.create(
                postulante=postulante,
                respuestas_detalle=respuestas,
                scores=scores,
                rol_principal=rol_principal,
                puntaje_total=puntaje_total
            )
            
            print(f"✅ Test guardado: Usuario {postulante.nombre_completo}, Rol: {rol_principal}, ID: {resultado.id}")
            
            return Response({
                "success": True,
                "message": "Test guardado correctamente",
                "resultado_id": resultado.id
            }, status=status.HTTP_201_CREATED)
            
        except Postulante.DoesNotExist:
            return Response(
                {"error": f"Usuario con ID {postulante_id} no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"❌ Error al guardar test: {str(e)}")
            return Response(
                {"error": f"Error al guardar test: {str(e)}"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class AdminView(APIView):
    def get(self, request):
        # Verificar si el usuario es admin
        admin_id = request.headers.get('X-Admin-ID')
        
        # Validar que admin_id sea un número entero válido
        if not admin_id:
            return Response({"error": "No autorizado - Admin ID requerido"}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            # Verificar que el usuario existe y sea admin
            admin = Postulante.objects.get(id=int(admin_id), es_admin=True)
        except (Postulante.DoesNotExist, ValueError):
            return Response({"error": "No autorizado - Usuario no es admin"}, status=status.HTTP_403_FORBIDDEN)
        
        # Obtener todos los resultados de tests (cualquier admin puede verlos todos)
        resultados = ResultadoTest.objects.select_related('postulante').all().order_by('-fecha_prueba')
        serializer = ResultadoTestSerializer(resultados, many=True)
        
        return Response({
            "success": True,
            "resultados": serializer.data
        }, status=status.HTTP_200_OK)

class EstadisticasView(APIView):
    """Obtener estadísticas de perfiles"""
    def get(self, request):
        admin_id = request.headers.get('X-Admin-ID')
        
        # Validar que admin_id sea un número entero válido
        if not admin_id:
            return Response({"error": "No autorizado - Admin ID requerido"}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            # Verificar que el usuario existe y sea admin
            admin = Postulante.objects.get(id=int(admin_id), es_admin=True)
        except (Postulante.DoesNotExist, ValueError):
            return Response({"error": "No autorizado - Usuario no es admin"}, status=status.HTTP_403_FORBIDDEN)
        
        # Contar perfiles
        resultados = ResultadoTest.objects.all()
        roles = [r.rol_principal for r in resultados if r.rol_principal]
        
        # Contar ocurrencias de cada rol
        conteo = Counter(roles)
        
        # Devolver con las letras A, B, C, D
        estadisticas = {
            'total_tests': resultados.count(),
            'perfiles': {
                'A': conteo.get('A', 0),
                'B': conteo.get('B', 0),
                'C': conteo.get('C', 0),
                'D': conteo.get('D', 0)
            }
        }
        
        return Response(estadisticas, status=status.HTTP_200_OK)