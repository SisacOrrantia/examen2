from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pendiente
from .serializers import (
    PendienteSerializer, 
    PendienteIDSerializer, 
    PendienteIDTitleSerializer, 
    PendienteIDUserSerializer
)

class PendienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo para CRUD de pendientes según los requerimientos de Parra's Dev
    """
    queryset = Pendiente.objects.all()
    serializer_class = PendienteSerializer

    @action(detail=False, methods=['get'], url_path='solo-ids')
    def solo_ids(self, request):
        """Lista de todos los pendientes (solo IDs)"""
        pendientes = self.get_queryset()
        serializer = PendienteIDSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de todos los pendientes (solo IDs)',
            'total': pendientes.count(),
            'data': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='ids-y-titulos')
    def ids_y_titulos(self, request):
        """Lista de todos los pendientes (IDs y Titles)"""
        pendientes = self.get_queryset()
        serializer = PendienteIDTitleSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de todos los pendientes (IDs y Títulos)',
            'total': pendientes.count(),
            'data': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='sin-resolver')
    def sin_resolver(self, request):
        """Lista de todos los pendientes sin resolver (ID y Title)"""
        pendientes = self.get_queryset().filter(completed=False)
        serializer = PendienteIDTitleSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de pendientes sin resolver (ID y Título)',
            'total': pendientes.count(),
            'data': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='resueltos')
    def resueltos(self, request):
        """Lista de todos los pendientes resueltos (ID y Title)"""
        pendientes = self.get_queryset().filter(completed=True)
        serializer = PendienteIDTitleSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de pendientes resueltos (ID y Título)',
            'total': pendientes.count(),
            'data': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='ids-y-usuarios')
    def ids_y_usuarios(self, request):
        """Lista de todos los pendientes (IDs y userID)"""
        pendientes = self.get_queryset()
        serializer = PendienteIDUserSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de todos los pendientes (IDs y Usuario)',
            'total': pendientes.count(),
            'data': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='resueltos-usuarios')
    def resueltos_usuarios(self, request):
        """Lista de todos los pendientes resueltos (ID y userID)"""
        pendientes = self.get_queryset().filter(completed=True)
        serializer = PendienteIDUserSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de pendientes resueltos (ID y Usuario)',
            'total': pendientes.count(),
            'data': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='sin-resolver-usuarios')
    def sin_resolver_usuarios(self, request):
        """Lista de todos los pendientes sin resolver (ID y userID)"""
        pendientes = self.get_queryset().filter(completed=False)
        serializer = PendienteIDUserSerializer(pendientes, many=True)
        return Response({
            'message': 'Lista de pendientes sin resolver (ID y Usuario)',
            'total': pendientes.count(),
            'data': serializer.data
        })

# Vistas Web para la interfaz
def dashboard(request):
    """Vista principal del dashboard"""
    pendientes = Pendiente.objects.all()
    stats = {
        'total': pendientes.count(),
        'completados': pendientes.filter(completed=True).count(),
        'sin_resolver': pendientes.filter(completed=False).count(),
        'usuarios': User.objects.count()
    }
    ultimos_pendientes = pendientes.order_by('-created_at')[:6]
    
    return render(request, 'pendientes/dashboard.html', {
        'stats': stats,
        'ultimos_pendientes': ultimos_pendientes
    })

# Vistas para cada tipo de lista
def solo_ids_view(request):
    """Vista web para solo IDs"""
    pendientes = Pendiente.objects.all()
    data = [{'id': p.id} for p in pendientes]
    return render(request, 'pendientes/solo_ids.html', {
        'data': data,
        'total': pendientes.count()
    })

def ids_titulos_view(request):
    """Vista web para IDs y títulos"""
    pendientes = Pendiente.objects.all()
    data = [{'id': p.id, 'title': p.title} for p in pendientes]
    return render(request, 'pendientes/ids_titulos.html', {
        'data': data,
        'total': pendientes.count()
    })

def sin_resolver_view(request):
    """Vista web para sin resolver"""
    pendientes = Pendiente.objects.filter(completed=False)
    data = [{'id': p.id, 'title': p.title} for p in pendientes]
    return render(request, 'pendientes/sin_resolver.html', {
        'data': data,
        'total': pendientes.count()
    })

def resueltos_view(request):
    """Vista web para resueltos"""
    pendientes = Pendiente.objects.filter(completed=True)
    data = [{'id': p.id, 'title': p.title} for p in pendientes]
    return render(request, 'pendientes/resueltos.html', {
        'data': data,
        'total': pendientes.count()
    })

def ids_usuarios_view(request):
    """Vista web para IDs y usuarios"""
    pendientes = Pendiente.objects.all()
    data = [{'id': p.id, 'user_id': p.user.id} for p in pendientes]
    return render(request, 'pendientes/ids_usuarios.html', {
        'data': data,
        'total': pendientes.count()
    })

def resueltos_usuarios_view(request):
    """Vista web para resueltos y usuarios"""
    pendientes = Pendiente.objects.filter(completed=True)
    data = [{'id': p.id, 'user_id': p.user.id} for p in pendientes]
    return render(request, 'pendientes/resueltos_usuarios.html', {
        'data': data,
        'total': pendientes.count()
    })

def sin_resolver_usuarios_view(request):
    """Vista web para sin resolver y usuarios"""
    pendientes = Pendiente.objects.filter(completed=False)
    data = [{'id': p.id, 'user_id': p.user.id} for p in pendientes]
    return render(request, 'pendientes/sin_resolver_usuarios.html', {
        'data': data,
        'total': pendientes.count()
    })

# Vistas CRUD
def crud_list_view(request):
    """Vista para listar todos los pendientes con opciones CRUD"""
    pendientes = Pendiente.objects.all().order_by('-created_at')
    completados = pendientes.filter(completed=True).count()
    sin_resolver = pendientes.filter(completed=False).count()
    
    return render(request, 'pendientes/crud_list.html', {
        'pendientes': pendientes,
        'completados': completados,
        'sin_resolver': sin_resolver
    })

def pendiente_detail_view(request, pk):
    """Vista para mostrar detalle de un pendiente"""
    pendiente = get_object_or_404(Pendiente, pk=pk)
    return render(request, 'pendientes/detail.html', {
        'pendiente': pendiente
    })

def pendiente_create_view(request):
    """Vista para crear un nuevo pendiente"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        user_id = request.POST.get('user')
        completed = request.POST.get('completed') == 'on'
        
        if title and user_id:
            user = get_object_or_404(User, pk=user_id)
            pendiente = Pendiente.objects.create(
                title=title,
                description=description,
                user=user,
                completed=completed
            )
            messages.success(request, f'Pendiente "{title}" creado exitosamente.')
            return redirect('pendientes:detail', pk=pendiente.pk)
        else:
            messages.error(request, 'Por favor completa todos los campos requeridos.')
    
    usuarios = User.objects.all().order_by('username')
    return render(request, 'pendientes/create.html', {
        'usuarios': usuarios
    })

def pendiente_update_view(request, pk):
    """Vista para editar un pendiente"""
    pendiente = get_object_or_404(Pendiente, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        user_id = request.POST.get('user')
        completed = request.POST.get('completed') == 'on'
        
        if title and user_id:
            user = get_object_or_404(User, pk=user_id)
            pendiente.title = title
            pendiente.description = description
            pendiente.user = user
            pendiente.completed = completed
            pendiente.save()
            
            messages.success(request, f'Pendiente "{title}" actualizado exitosamente.')
            return redirect('pendientes:detail', pk=pendiente.pk)
        else:
            messages.error(request, 'Por favor completa todos los campos requeridos.')
    
    usuarios = User.objects.all().order_by('username')
    return render(request, 'pendientes/update.html', {
        'pendiente': pendiente,
        'usuarios': usuarios
    })
