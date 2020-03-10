from django.contrib import admin
from .models import Receita


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'time',
                    'creation_date', 'owner_person', 'visible')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('visible',)
    list_per_page = 3


admin.site.register(Receita, ReceitaAdmin)
