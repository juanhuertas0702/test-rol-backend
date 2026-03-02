#!/usr/bin/env python
"""
Script para crear/actualizar el usuario admin en la base de datos
Ejecutar: python setup_admin.py
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from evaluacion.models import Postulante

# Datos del admin
ADMIN_NAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# Eliminar admin antiguo si existe (para resetearlo)
Postulante.objects.filter(nombre_completo='admin', es_admin=True).delete()

# Crear nuevo admin
admin = Postulante.objects.create(
    nombre_completo=ADMIN_NAME,
    contrasena=make_password(ADMIN_PASSWORD),
    es_admin=True,
    id_usuario=None
)

print(f"✅ Usuario admin creado exitosamente:")
print(f"   Nombre: {ADMIN_NAME}")
print(f"   Contraseña: {ADMIN_PASSWORD}")
print(f"   ID: {admin.id}")

# También crear usuario de prueba si no existe
juan = Postulante.objects.filter(nombre_completo='Juan', id_usuario='12345', es_admin=False).first()
if not juan:
    juan = Postulante.objects.create(
        nombre_completo='Juan',
        id_usuario='12345',
        es_admin=False
    )
    print(f"\n✅ Usuario de prueba creado:")
    print(f"   Nombre: Juan")
    print(f"   ID: 12345")
