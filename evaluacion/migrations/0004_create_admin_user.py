# Generated migration to create admin user

from django.db import migrations


def create_admin_user(apps, schema_editor):
    """Crear el usuario admin de ejemplo si no existe"""
    Postulante = apps.get_model('evaluacion', 'Postulante')
    
    # Crear usuario admin solo si no existe
    if not Postulante.objects.filter(id_usuario='12345').exists():
        Postulante.objects.create(
            nombre_completo='Juan',
            id_usuario='12345',
            es_admin=True
        )


def reverse_admin_user(apps, schema_editor):
    """Eliminar el usuario admin de ejemplo"""
    Postulante = apps.get_model('evaluacion', 'Postulante')
    Postulante.objects.filter(id_usuario='12345').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0003_postulante_model_update'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, reverse_admin_user),
    ]
