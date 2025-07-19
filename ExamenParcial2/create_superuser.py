from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@parrasdev.com', 'admin123')
print("Superusuario creado exitosamente")
