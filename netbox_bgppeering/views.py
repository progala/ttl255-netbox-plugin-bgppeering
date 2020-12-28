from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.edit import CreateView
from django_tables2 import LazyPaginator, RequestConfig, SingleTableView

from .filters import BgpPeeringFilter
from .forms import BgpPeeringForm, BgpPeeringFilterForm
from .models import BgpPeering
from .tables import BgpPeeringTable
from .icon_classes import icon_classes


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
    filterset = BgpPeeringFilter
    filterset_form = BgpPeeringFilterForm

    def get(self, request):
        """Get request."""

        self.queryset = self.filterset(request.GET, self.queryset).qs

        table = BgpPeeringTable(self.queryset)
        RequestConfig(request, paginate={"per_page": 25}).configure(table)

        return render(
            request,
            "netbox_bgppeering/bgppeering_list.html",
            {
                "table": table,
                "filter_form": self.filterset_form(request.GET),
                "icon_classes": icon_classes,
            },
        )


class BgpPeeringCreateView(CreateView):
    """View for creating a new BgpPeering instance."""

    form_class = BgpPeeringForm
    template_name = "netbox_bgppeering/bgppeering_edit.html"
