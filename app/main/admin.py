from django.contrib import admin
from .models import *

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', )
    search_fields = ('name', )


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', 'contracts')
    search_fields = ('name', )


class PermissionContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'position')


class SubsidiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user', )


class SubcontractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user', )


admin.site.register(Contract, ContractAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(PermissionContract, PermissionContractAdmin)
admin.site.register(Subsidiary, SubsidiaryAdmin)
admin.site.register(Subcontractor, SubcontractorAdmin)
