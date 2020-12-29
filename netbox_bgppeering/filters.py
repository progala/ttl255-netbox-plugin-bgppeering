import django_filters
from django.db.models import Q

from dcim.models import Device, Site

from .models import BgpPeering


class BgpPeeringFilter(django_filters.FilterSet):
    """Filter capabilities for BgpPeering instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    site = django_filters.ModelMultipleChoiceFilter(
        field_name="site__slug",
        queryset=Site.objects.all(),
        to_field_name="slug",
    )

    device = django_filters.ModelMultipleChoiceFilter(
        field_name="device__name",
        queryset=Device.objects.all(),
        to_field_name="name",
    )

    peer_name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    class Meta:
        model = BgpPeering

        fields = [
            "local_as",
            "remote_as",
            "peer_name",
        ]

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(peer_name__icontains=value) | Q(description__icontains=value)
        return queryset.filter(qs_filter)
