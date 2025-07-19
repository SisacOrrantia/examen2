from rest_framework import serializers
from .models import Pendiente

class PendienteSerializer(serializers.ModelSerializer):
    """Serializador completo para pendientes"""
    class Meta:
        model = Pendiente
        fields = '__all__'

class PendienteIDSerializer(serializers.ModelSerializer):
    """Serializador solo con IDs"""
    class Meta:
        model = Pendiente
        fields = ['id']

class PendienteIDTitleSerializer(serializers.ModelSerializer):
    """Serializador con ID y título"""
    class Meta:
        model = Pendiente
        fields = ['id', 'title']

class PendienteIDUserSerializer(serializers.ModelSerializer):
    """Serializador con ID y usuario"""
    user_id = serializers.IntegerField(source='user.id')
    
    class Meta:
        model = Pendiente
        fields = ['id', 'user_id']
