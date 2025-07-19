# 🚀 Parra's Dev - Sistema de Gestión de Pendientes

## 📋 Descripción
Sistema desarrollado para **Parra's Dev** que resuelve el problema de la pizarra de pendientes mediante una API REST robusta y funcional. La aplicación contempla el control completo de la lista de pendientes (ToDo) según los requerimientos específicos.

## 🎯 Funcionalidades Implementadas

### ✅ APIs Solicitadas (Todas Implementadas)
1. **Lista de todos los pendientes (solo IDs)** - `/api/pendientes/solo-ids/`
2. **Lista de todos los pendientes (IDs y Titles)** - `/api/pendientes/ids-y-titulos/`
3. **Lista de todos los pendientes sin resolver (ID y Title)** - `/api/pendientes/sin-resolver/`
4. **Lista de todos los pendientes resueltos (ID y Title)** - `/api/pendientes/resueltos/`
5. **Lista de todos los pendientes (IDs y userID)** - `/api/pendientes/ids-y-usuarios/`
6. **Lista de todos los pendientes resueltos (ID y userID)** - `/api/pendientes/resueltos-usuarios/`
7. **Lista de todos los pendientes sin resolver (ID y userID)** - `/api/pendientes/sin-resolver-usuarios/`

### ⚙️ Operaciones CRUD Completas
- **CREATE**: `POST /api/pendientes/`
- **READ**: `GET /api/pendientes/` (todos) | `GET /api/pendientes/{id}/` (específico)
- **UPDATE**: `PUT /api/pendientes/{id}/` (completo) | `PATCH /api/pendientes/{id}/` (parcial)
- **DELETE**: `DELETE /api/pendientes/{id}/`

## 🛠️ Tecnologías Utilizadas
- **Backend**: Django 5.2.4 + Django REST Framework
- **Base de Datos**: SQLite (con datos en español)
- **Frontend**: HTML5 + CSS3 + JavaScript (diseño básico gris/rojo)
- **API**: REST con documentación automática

## 🚀 Instalación y Uso

### 1. Activar el entorno virtual
```bash
# El entorno ya está configurado en:
C:/Users/misam/OneDrive/Escritorio/ExamenParcial2/venv/Scripts/activate
```

### 2. Ejecutar el servidor
```bash
python manage.py runserver
```

### 3. Acceder a la aplicación
- **Dashboard Principal**: http://127.0.0.1:8000/
- **API Browser**: http://127.0.0.1:8000/api/
- **Panel Admin**: http://127.0.0.1:8000/admin/

## 👥 Usuarios de Prueba

### Administrador
- **Usuario**: `admin`
- **Contraseña**: `admin123`
- **Email**: `admin@parrasdev.com`

### Usuarios Adicionales
| Usuario | Contraseña | Email |
|---------|------------|-------|
| maria_garcia | password123 | maria@parrasdev.com |
| juan_perez | password123 | juan@parrasdev.com |
| ana_rodriguez | password123 | ana@parrasdev.com |
| carlos_lopez | password123 | carlos@parrasdev.com |

## 📊 Datos de Ejemplo
La base de datos incluye **20 pendientes** en español con:
- **8 tareas completadas**
- **12 tareas pendientes**
- Asignadas a **5 usuarios diferentes**
- Contenido realista para pruebas

## 🎨 Diseño
- **Colores principales**: Gris (#6c757d) y Rojo (#dc3545)
- **Estilo**: Básico, funcional y sin complicaciones
- **Responsive**: Adaptable a dispositivos móviles
- **UX**: Simple e intuitivo

## 📖 Endpoints Principales

### Lista Completa de APIs
```
GET /api/pendientes/solo-ids/           # Solo IDs
GET /api/pendientes/ids-y-titulos/      # IDs + Títulos
GET /api/pendientes/sin-resolver/       # Sin resolver (ID + Title)
GET /api/pendientes/resueltos/          # Resueltos (ID + Title)
GET /api/pendientes/ids-y-usuarios/     # IDs + UserIDs
GET /api/pendientes/resueltos-usuarios/ # Resueltos + UserIDs
GET /api/pendientes/sin-resolver-usuarios/ # Sin resolver + UserIDs
```

### CRUD Principal
```
GET    /api/pendientes/     # Listar todos
POST   /api/pendientes/     # Crear nuevo
GET    /api/pendientes/{id} # Ver específico
PUT    /api/pendientes/{id} # Actualizar completo
PATCH  /api/pendientes/{id} # Actualizar parcial
DELETE /api/pendientes/{id} # Eliminar
```

## 📋 Ejemplo de Uso

### Crear un nuevo pendiente
```bash
curl -X POST http://127.0.0.1:8000/api/pendientes/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nueva tarea importante",
    "description": "Descripción detallada de la tarea",
    "user": 1,
    "completed": false
  }'
```

### Obtener pendientes sin resolver
```bash
curl http://127.0.0.1:8000/api/pendientes/sin-resolver/
```

## 🔧 Estructura del Proyecto
```
ExamenParcial2/
├── manage.py
├── parras_dev_project/        # Configuración principal
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pendientes/                # App principal
│   ├── models.py             # Modelo Pendiente
│   ├── serializers.py        # Serializadores DRF
│   ├── views.py              # ViewSets y APIs
│   ├── urls.py               # URLs de la app
│   └── admin.py              # Configuración admin
├── templates/                # Templates HTML
│   └── pendientes/
│       └── dashboard.html
├── static/                   # Archivos estáticos
│   └── css/
│       └── style.css
└── db.sqlite3               # Base de datos SQLite
```

## 📈 Calidad del Código
- ✅ Modelos bien estructurados con relaciones apropiadas
- ✅ Serializadores específicos para cada endpoint
- ✅ ViewSets organizados con acciones personalizadas
- ✅ URLs limpias y semánticas
- ✅ Documentación automática de la API
- ✅ Diseño responsive y accesible

## 🎯 Cumplimiento de Requerimientos
✅ **Control completo de lista de pendientes**  
✅ **Todas las 7 listas solicitadas implementadas**  
✅ **CRUD completo funcionando**  
✅ **Base de datos SQLite con datos en español**  
✅ **Diseño básico gris/rojo sin complicaciones**  
✅ **API REST profesional**  
✅ **Código fuente de calidad**  

---

**Desarrollado para Parra's Dev** 🚀  
*Información oportuna y confiable para tomar las mejores decisiones*
