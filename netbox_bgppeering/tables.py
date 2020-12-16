import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn
from .models import BgpPeering


class BgpPeeringTable(BaseTable):
    """Table for displaying BGP Peering objects."""

    pk = ToggleColumn()
    id = tables.LinkColumn()
    site = tables.LinkColumn()
    device = tables.LinkColumn()
    local_ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = BgpPeering
        fields = (
            "pk",
            "id",
            "site",
            "device",
            "local_ip",
            "peer_name",
            "remote_ip",
            "remote_as",
        )
