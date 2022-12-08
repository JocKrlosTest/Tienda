from django.contrib import admin
from Usuarios.models import Usuario
#from django.contrib import admin
# account
# Register your models here.
admin.site.site_header = "Tienda"
admin.site.site_title = "Administracion"
admin.site.index_title = "Tienda"


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','username','telefono')
    ordering = ("last_name",'first_name')
    exclude = ("is_active","date_joined","last_login")