#!/usr/bin/env python
"""
Script para crear el usuario admin de ejemplo (Juan id:12345)
Ejecutar con: python manage.py shell < create_admin_user.py
O dentro de shell:
    exec(open('create_admin_user.py').read())
"""

from evaluacion.models import Postulante

# Eliminar usuario si ya existe
Postulante.objects.filter(id_usuario='12345').delete()

# Crear usuario admin de ejemplo
admin_user = Postulante.objects.create(
    nombre_completo='Juan',
    id_usuario='12345',
    es_admin=True
)

print(f"✅ Usuario admin creado exitosamente:")
print(f"   Nombre: {admin_user.nombre_completo}")
print(f"   ID Usuario: {admin_user.id_usuario}")
print(f"   Es Admin: {admin_user.es_admin}")
print(f"\nPuedes iniciar sesión con:")
print(f"   Nombre: Juan")
print(f"   ID: 12345")
