from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router para las APIs
router = DefaultRouter()
router.register(r'pendientes', views.PendienteViewSet)

app_name = 'pendientes'

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Vista web principal
    path('', views.dashboard, name='dashboard'),
    
    # Vistas web para cada tipo de lista (según requerimientos)
    path('listas/solo-ids/', views.solo_ids_view, name='solo_ids'),
    path('listas/ids-titulos/', views.ids_titulos_view, name='ids_titulos'),
    path('listas/sin-resolver/', views.sin_resolver_view, name='sin_resolver'),
    path('listas/resueltos/', views.resueltos_view, name='resueltos'),
    path('listas/ids-usuarios/', views.ids_usuarios_view, name='ids_usuarios'),
    path('listas/resueltos-usuarios/', views.resueltos_usuarios_view, name='resueltos_usuarios'),
    path('listas/sin-resolver-usuarios/', views.sin_resolver_usuarios_view, name='sin_resolver_usuarios'),
    
    # CRUD completo
    path('crud/', views.crud_list_view, name='crud_list'),
    path('crud/crear/', views.pendiente_create_view, name='create'),
    path('crud/<int:pk>/', views.pendiente_detail_view, name='detail'),
    path('crud/<int:pk>/editar/', views.pendiente_update_view, name='update'),
]
