# Generated migration to create users

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_users(apps, schema_editor):
    """Crear usuarios de ejemplo"""
    Postulante = apps.get_model('evaluacion', 'Postulante')
    
    # Eliminar usuarios anteriores si existen
    Postulante.objects.filter(nombre_completo__in=['Juan', 'María']).delete()
    
    # Crear usuario normal Juan
    Postulante.objects.create(
        nombre_completo='Juan',
        id_usuario='12345',
        es_admin=False
    )
    
    # Crear usuario admin María con contraseña
    Postulante.objects.create(
        nombre_completo='María',
        contrasena=make_password('12345'),
        es_admin=True
    )


def reverse_users(apps, schema_editor):
    """Eliminar usuarios de ejemplo"""
    Postulante = apps.get_model('evaluacion', 'Postulante')
    Postulante.objects.filter(nombre_completo__in=['Juan', 'María']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0005_postulante_password'),
    ]

    operations = [
        migrations.RunPython(create_users, reverse_users),
    ]
