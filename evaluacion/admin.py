from django.contrib import admin
from .models import Postulante, ResultadoTest

@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'id_usuario', 'es_admin', 'fecha_registro')
    list_filter = ('es_admin', 'fecha_registro')
    search_fields = ('nombre_completo', 'id_usuario')
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_completo', 'id_usuario')
        }),
        ('Seguridad', {
            'fields': ('contrasena', 'es_admin')
        }),
        ('Metadata', {
            'fields': ('fecha_registro',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('fecha_registro',)

@admin.register(ResultadoTest)
class ResultadoTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'postulante', 'puntaje_total', 'fecha_prueba')
    list_filter = ('fecha_prueba', 'puntaje_total')
    search_fields = ('postulante__nombre_completo',)
    readonly_fields = ('fecha_prueba',)
