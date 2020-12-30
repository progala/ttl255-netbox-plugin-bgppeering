import django_tables2 as tables
from utilities.tables import BaseTable
from .models import BgpPeering


class BgpPeeringTable(BaseTable):
    """Table for displaying BGP Peering objects."""

    id = tables.LinkColumn()
    site = tables.LinkColumn()
    device = tables.LinkColumn()
    local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = BgpPeering
        fields = (
            "id",
            "site",
            "device",
            "local_ip",
            "peer_name",
            "remote_ip",
            "remote_as",
        )
