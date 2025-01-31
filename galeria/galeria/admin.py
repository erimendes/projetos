from django.contrib import admin
from galeria.models import Fotografia

# Definindo uma classe com um nome mais convencional para administração
class FotografiaAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de objetos
    list_display = ("id", "nome", "legenda", "publicada")
    
    # Campos que serão clicáveis para editar a fotografia
    list_display_links = ("id", "nome", "legenda")
    
    # Habilitando a busca pelo nome da fotografia
    search_fields = ("nome",)

    list_filter = ("categoria",)
    list_editable = ("publicada",)

    list_per_page = 1

# Registrando o modelo 'Fotografia' com a configuração personalizada
admin.site.register(Fotografia, FotografiaAdmin)
