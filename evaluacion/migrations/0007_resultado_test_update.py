# Auto-generated migration for ResultadoTest model changes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0006_create_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadotest',
            name='scores',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='resultadotest',
            name='rol_principal',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='resultadotest',
            name='puntaje_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resultadotest',
            name='respuestas_detalle',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterModelOptions(
            name='resultadotest',
            options={'ordering': ['-fecha_prueba']},
        ),
    ]
