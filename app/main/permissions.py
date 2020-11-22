from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Permission

class SubsidiaryPermission(BasePermission):
    '''
    Переопределение метода разграничения прав
    codename указан в качестве примера
    '''
    def has_permission(self, request, view):
        if request.method == 'GET':
            return bool(request.user.user_permissions.filter(codename='add_subsidiary').first() and request.user.is_authenticated)


class SubcontractorPermission(BasePermission):
    '''
    Переопределение метода разграничения прав
    codename указан в качестве примера
    '''
    def has_permission(self, request, view):
        if request.method == 'GET':
            return bool(request.user.user_permissions.filter(codename='add_subcontractor').first() and request.user.is_authenticated)
