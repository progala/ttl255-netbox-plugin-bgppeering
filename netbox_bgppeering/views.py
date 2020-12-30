from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import LazyPaginator, RequestConfig, SingleTableView

from .icon_classes import icon_classes
from .filters import BgpPeeringFilter
from .forms import BgpPeeringForm, BgpPeeringFilterForm
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
                "icon_classes": icon_classes,
            },
        )


class BgpPeeringListView(View):
    """View for listing all existing BGP Peerings."""

    queryset = BgpPeering.objects.all()
    filterset = BgpPeeringFilter
    filterset_form = BgpPeeringFilterForm

    def get(self, request):
        """Get request."""

        self.queryset = self.filterset(request.GET, self.queryset).qs.order_by("pk")

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


class BgpPeeringDeleteView(DeleteView):
    """View for deleting a BgpPeering instance."""

    model = BgpPeering
    success_url = reverse_lazy("plugins:netbox_bgppeering:bgppeering_list")
    template_name = "netbox_bgppeering/bgppeering_delete.html"


class BgpPeeringEditView(UpdateView):
    """View for editing a BgpPeering instance."""

    model = BgpPeering
    form_class = BgpPeeringForm
    template_name = "netbox_bgppeering/bgppeering_edit.html"
