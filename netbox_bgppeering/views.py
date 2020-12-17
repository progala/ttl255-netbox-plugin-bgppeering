from django.shortcuts import get_object_or_404, render

from utilities.views import ObjectView, ObjectEditView, ObjectListView

from .forms import BgpPeeringForm
from .models import BgpPeering
from .tables import BgpPeeringTable


class BgpPeeringView(ObjectView):
    """Display BGP Peering details"""

    queryset = BgpPeering.objects.all()

    def get(self, request, pk):
        """Get request."""
        bgppeering_obj = get_object_or_404(self.queryset, pk=pk)

        return render(
            request,
            "netbox_bgppeering/bgppeering.html",
            {
                "bgppeering": bgppeering_obj,
            },
        )


class BgpPeeringListView(ObjectListView):
    """View for listing all existing BGP Peerings."""

    queryset = BgpPeering.objects.all()
    table = BgpPeeringTable
    template_name = "netbox_bgppeering/bgppeering_list.html"


class BgpPeeringCreateView(ObjectEditView):
    """View for creating a new BgpPeering instance."""

    queryset = BgpPeering.objects.all()
    model_form = BgpPeeringForm
    template_name = "netbox_bgppeering/bgppeering_edit.html"
    default_return_url = "plugins:netbox_bgppeering:bgppeering_add"
