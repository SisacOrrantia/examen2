from django.db import models
from django.contrib.auth.models import User

class Pendiente(models.Model):
    """
    Modelo para representar un pendiente (ToDo) en el sistema de Parra's Dev
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    completed = models.BooleanField(default=False, verbose_name="Completado")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "Pendiente"
        verbose_name_plural = "Pendientes"
        ordering = ['-created_at']
    
    def __str__(self):
        status = "✅" if self.completed else "⏳"
        return f"{status} {self.title}"
