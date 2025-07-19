from django.contrib import admin
from .models import Pendiente

@admin.register(Pendiente)
class PendienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'completed', 'created_at']
    list_filter = ['completed', 'created_at', 'user']
    search_fields = ['title', 'description']
    list_editable = ['completed']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'description', 'user')
        }),
        ('Estado', {
            'fields': ('completed',)
        }),
    )
