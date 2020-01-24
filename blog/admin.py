from django.contrib import admin
from .models import Post, Marca, Automovil

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'anio', 'modelo')
    search_fields = ['patente', 'modelo']


admin.site.register(Post)
admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)


# Register your models here.

