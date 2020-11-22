from rest_framework import routers
from .api import *


router = routers.SimpleRouter()
router.register('api/contract', ContractViewSet, 'contract')
router.register('api/position', PositionViewSet, 'position')
router.register('api/permissioncontract', PermissionContractViewSet, 'permissioncontract')
router.register('api/subsidiary', SubsidiaryViewSet, 'subsidiary')
router.register('api/subcontractor', SubcontractorViewSet, 'subcontractor')

urlpatterns = router.urls