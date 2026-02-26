#!/usr/bin/env python
"""
Script para verificar y crear el usuario admin
Ejecutar dentro de Django shell: python manage.py shell < verify_user.py
"""

from evaluacion.models import Postulante

# Verificar si el usuario existe
try:
    usuario = Postulante.objects.get(id_usuario='12345')
    print(f"✅ Usuario encontrado:")
    print(f"   Nombre: {usuario.nombre_completo}")
    print(f"   ID: {usuario.id_usuario}")
    print(f"   Es Admin: {usuario.es_admin}")
except Postulante.DoesNotExist:
    print("❌ Usuario no encontrado, creando...")
    
    # Crear el usuario
    usuario = Postulante.objects.create(
        nombre_completo='Juan',
        id_usuario='12345',
        es_admin=True
    )
    print(f"✅ Usuario creado exitosamente:")
    print(f"   Nombre: {usuario.nombre_completo}")
    print(f"   ID: {usuario.id_usuario}")
    print(f"   Es Admin: {usuario.es_admin}")

print("\n📝 Puedes iniciar sesión con:")
print("   Nombre: Juan")
print("   ID Usuario: 12345")
