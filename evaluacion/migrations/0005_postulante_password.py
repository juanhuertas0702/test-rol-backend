# Auto-generated migration for Postulante model changes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0004_create_admin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante',
            name='id_usuario',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='postulante',
            name='contrasena',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
