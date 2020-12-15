from django.shortcuts import get_object_or_404, render

from utilities.views import ObjectView

from .models import BgpPeering


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
