# Auto-generated migration for Postulante model changes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0002_postulante_contrasena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulante',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='postulante',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='postulante',
            name='contrasena',
        ),
        migrations.AddField(
            model_name='postulante',
            name='id_usuario',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postulante',
            name='es_admin',
            field=models.BooleanField(default=False),
        ),
    ]
