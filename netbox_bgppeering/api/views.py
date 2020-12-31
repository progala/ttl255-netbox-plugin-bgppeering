from rest_framework import mixins, viewsets

from netbox_bgppeering.models import BgpPeering
from netbox_bgppeering.filters import BgpPeeringFilter

from .serializers import BgpPeeringSerializer


class BgpPeeringView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Create, check status of, update, and delete BgpPeering object."""

    queryset = BgpPeering.objects.all()
    filterset_class = BgpPeeringFilter
    serializer_class = BgpPeeringSerializer
