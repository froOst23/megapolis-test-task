from .models import *
from .serializer import *
from .permissions import SubsidiaryPermission, SubcontractorPermission
from rest_framework import viewsets, permissions, response
from django.contrib.auth.models import Permission
from .models import *


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = ContractSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = PositionSerializer


class PermissionContractViewSet(viewsets.ModelViewSet):
    queryset = PermissionContract.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = PermissionContractSerializer


class SubsidiaryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        SubsidiaryPermission
    ]
    serializer_class = SubsidiarySerializer

    def get_queryset(self):
        '''
        Переопределяем метод для того чтобы показывать договоры
        только для пользователя совершившего вход
        '''
        current_user = self.request.user.id
        return Subsidiary.objects.filter(user=current_user)


class SubcontractorViewSet(viewsets.ModelViewSet):
    permission_classes = [
        SubcontractorPermission
    ]
    serializer_class = SubcontractorSerializer

    def get_queryset(self):
        '''
        Переопределяем метод для того чтобы показывать договоры
        только для пользователя совершившего вход
        '''
        current_user = self.request.user.id
        return Subcontractor.objects.filter(user=current_user)
