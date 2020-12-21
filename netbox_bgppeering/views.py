from django.shortcuts import get_object_or_404, render
from django.views import View
from django_tables2 import LazyPaginator, RequestConfig, SingleTableView

from utilities.views import ObjectEditView

from .forms import BgpPeeringForm
from .models import BgpPeering
from .tables import BgpPeeringTable


class BgpPeeringView(View):
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


class BgpPeeringListView(View):
    """View for listing all existing BGP Peerings."""

    queryset = BgpPeering.objects.all()

    def get(self, request):
        """Get request."""
        table = BgpPeeringTable(self.queryset)
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        return render(
            request, "netbox_bgppeering/bgppeering_list.html", {"table": table}
        )


class BgpPeeringCreateView(ObjectEditView):
    """View for creating a new BgpPeering instance."""

    queryset = BgpPeering.objects.all()
    model_form = BgpPeeringForm
    template_name = "netbox_bgppeering/bgppeering_edit.html"
