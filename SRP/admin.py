from django.contrib import admin
from .models import Praktyki, Grupa


@admin.register(Praktyki)
class PraktykiAdmin(admin.ModelAdmin):
    list_display = (
            'id_Praktyki', 'stanowisko', 'id_Firma'
    )


@admin.register(Grupa)
class GrupaAdmin(admin.ModelAdmin):
    list_display = (
        'id_Praktyki', 'uczestnik'
    )
