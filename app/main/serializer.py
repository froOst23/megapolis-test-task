from rest_framework import serializers
from .models import *

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'name')
        ordering = ['-id']


class PositionSerializer(serializers.ModelSerializer):
    contracts = ContractSerializer(many=True, read_only=True)
    class Meta:
        model = Position
        fields = ('id', 'name', 'contracts')
        ordering = ['-id']
    

class PermissionContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionContract
        fields = ('id', 'contract', 'position')
        ordering = ['-id']


class SubsidiarySerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    class Meta:
        model = Subsidiary
        fields = ('id', 'user', 'position')
        ordering = ['-id']


class SubcontractorSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    class Meta:
        model = Subcontractor
        fields = ('id', 'user', 'position')
        ordering = ['-id']
