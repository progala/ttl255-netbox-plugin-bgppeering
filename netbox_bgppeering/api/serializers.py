from rest_framework import serializers

from dcim.models import Site, Device
from ipam.api.nested_serializers import (
    NestedIPAddressSerializer,
)
from dcim.api.nested_serializers import NestedDeviceSerializer, NestedSiteSerializer

from netbox_bgppeering.models import BgpPeering


class BgpPeeringSerializer(serializers.ModelSerializer):
    """Serializer for the BgpPeering model."""

    site = NestedSiteSerializer(
        many=False,
        read_only=False,
        required=False,
        help_text="BgpPeering Site",
    )

    device = NestedDeviceSerializer(
        many=False,
        read_only=False,
        required=True,
        help_text="BgpPeering Device",
    )

    local_ip = NestedIPAddressSerializer(
        many=False,
        read_only=False,
        required=True,
        help_text="Local peering IP",
    )

    class Meta:
        model = BgpPeering
        fields = [
            "id",
            "site",
            "device",
            "local_ip",
            "local_as",
            "remote_ip",
            "remote_as",
            "peer_name",
            "description",
        ]
