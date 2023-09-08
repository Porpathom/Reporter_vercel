from django.contrib import admin 
from web.models import Reporter, Art
# Register your models here.
admin.site.register(Reporter)

class ReporterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)
    search_fields = list_display
    
admin.site.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ("head_line","pub_date","reporter")
    search_fields = list_display
    
