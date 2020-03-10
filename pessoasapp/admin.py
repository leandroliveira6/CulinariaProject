from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email',)
  list_display_links = ('id', 'name', )
  search_fields = ('name',)
  list_per_page = 3

admin.site.register(Pessoa, PessoaAdmin)