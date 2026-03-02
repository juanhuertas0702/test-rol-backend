#!/usr/bin/env python
"""
Script de prueba para verificar el flujo completo del test
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from evaluacion.models import Postulante, ResultadoTest
from django.utils import timezone

print("=" * 60)
print("VERIFICACIÓN DEL SISTEMA DE TEST")
print("=" * 60)

# 1. Verificar usuarios
print("\n1️⃣ USUARIOS EN LA BASE DE DATOS:")
usuarios = Postulante.objects.all()
for u in usuarios:
    print(f"   - {u.nombre_completo} (ID: {u.id}, Admin: {u.es_admin})")

# 2. Verificar pruebas guardadas
print("\n2️⃣ PRUEBAS COMPLETADAS:")
pruebas = ResultadoTest.objects.select_related('postulante').all()
if pruebas.count() == 0:
    print("   ⚠️  No hay pruebas guardadas aún")
else:
    for p in pruebas:
        print(f"   - {p.postulante.nombre_completo}: {p.rol_principal} ({p.puntaje_total} pts)")
        print(f"     Fecha: {p.fecha_prueba.strftime('%d/%m/%Y %H:%M:%S')}")

# 3. Estadísticas
print("\n3️⃣ ESTADÍSTICAS DE PERFILES:")
from collections import Counter
roles = [p.rol_principal for p in pruebas if p.rol_principal]
conteo = Counter(roles)
for role in ['A', 'B', 'C', 'D']:
    print(f"   {role}: {conteo.get(role, 0)}")

# 4. Resumen
print("\n4️⃣ RESUMEN:")
print(f"   Total usuarios: {Postulante.objects.count()}")
print(f"   Total pruebas completadas: {pruebas.count()}")
print(f"   Puntaje promedio: {sum(p.puntaje_total for p in pruebas) / pruebas.count() if pruebas.count() > 0 else 0:.1f}")

print("\n" + "=" * 60)
print("✅ Verificación completada")
print("=" * 60)
