from rest_framework import routers
from .views import BgpPeeringView

router = routers.DefaultRouter()

router.register(r"bgppeering", BgpPeeringView)

urlpatterns = router.urls
