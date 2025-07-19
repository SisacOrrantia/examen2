from django.contrib.auth.models import User
from pendientes.models import Pendiente

# Crear usuarios adicionales
users_data = [
    {'username': 'maria_garcia', 'email': 'maria@parrasdev.com', 'password': 'password123', 'first_name': 'María', 'last_name': 'García'},
    {'username': 'juan_perez', 'email': 'juan@parrasdev.com', 'password': 'password123', 'first_name': 'Juan', 'last_name': 'Pérez'},
    {'username': 'ana_rodriguez', 'email': 'ana@parrasdev.com', 'password': 'password123', 'first_name': 'Ana', 'last_name': 'Rodríguez'},
    {'username': 'carlos_lopez', 'email': 'carlos@parrasdev.com', 'password': 'password123', 'first_name': 'Carlos', 'last_name': 'López'},
]

created_users = []
for user_data in users_data:
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults={
            'email': user_data['email'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name']
        }
    )
    if created:
        user.set_password(user_data['password'])
        user.save()
        print(f"Usuario {user.username} creado")
    created_users.append(user)

# Obtener todos los usuarios incluyendo admin
all_users = User.objects.all()

# Crear pendientes de ejemplo en español
pendientes_data = [
    {'title': 'Desarrollar API REST para inventario', 'description': 'Crear endpoints para gestión de productos', 'completed': False},
    {'title': 'Implementar autenticación JWT', 'description': 'Agregar sistema de tokens para seguridad', 'completed': True},
    {'title': 'Diseñar base de datos de clientes', 'description': 'Crear modelo entidad-relación para CRM', 'completed': False},
    {'title': 'Configurar servidor de producción', 'description': 'Deployer aplicación en AWS', 'completed': True},
    {'title': 'Crear documentación técnica', 'description': 'Documentar todos los endpoints de la API', 'completed': False},
    {'title': 'Optimizar consultas de base de datos', 'description': 'Mejorar rendimiento con índices', 'completed': True},
    {'title': 'Implementar sistema de notificaciones', 'description': 'Envío de emails automáticos', 'completed': False},
    {'title': 'Realizar pruebas unitarias', 'description': 'Cobertura mínima del 80%', 'completed': False},
    {'title': 'Integrar sistema de pagos', 'description': 'Conexión con PayPal y Stripe', 'completed': True},
    {'title': 'Desarrollar panel de administración', 'description': 'Interface para gestión de usuarios', 'completed': False},
    {'title': 'Configurar backup automático', 'description': 'Respaldo diario de la base de datos', 'completed': True},
    {'title': 'Implementar cache Redis', 'description': 'Mejorar velocidad de respuesta', 'completed': False},
    {'title': 'Crear aplicación móvil', 'description': 'App nativa para iOS y Android', 'completed': False},
    {'title': 'Configurar monitoring', 'description': 'Alertas para errores del sistema', 'completed': True},
    {'title': 'Actualizar dependencias', 'description': 'Mantener librerías actualizadas', 'completed': False},
    {'title': 'Implementar búsqueda avanzada', 'description': 'Filtros y ordenamiento completo', 'completed': False},
    {'title': 'Crear sistema de reportes', 'description': 'Generar PDFs con estadísticas', 'completed': True},
    {'title': 'Optimizar interfaz de usuario', 'description': 'Mejorar UX/UI del dashboard', 'completed': False},
    {'title': 'Configurar CI/CD', 'description': 'Pipeline automatizado de deployment', 'completed': True},
    {'title': 'Implementar websockets', 'description': 'Comunicación en tiempo real', 'completed': False},
]

# Asignar pendientes a usuarios aleatoriamente
import random
for i, pendiente_data in enumerate(pendientes_data):
    user = all_users[i % len(all_users)]
    pendiente, created = Pendiente.objects.get_or_create(
        title=pendiente_data['title'],
        defaults={
            'description': pendiente_data['description'],
            'completed': pendiente_data['completed'],
            'user': user
        }
    )
    if created:
        print(f"Pendiente '{pendiente.title}' creado para {user.username}")

print(f"\n✅ Datos de prueba creados exitosamente!")
print(f"👥 Usuarios: {User.objects.count()}")
print(f"📋 Pendientes: {Pendiente.objects.count()}")
print(f"✅ Completados: {Pendiente.objects.filter(completed=True).count()}")
print(f"⏳ Pendientes: {Pendiente.objects.filter(completed=False).count()}")
