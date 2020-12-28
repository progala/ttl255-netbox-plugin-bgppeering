from django import forms

from dcim.models import Device, Site
from utilities.forms import BootstrapMixin

from .models import BgpPeering


class BgpPeeringForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new BgpPeering object."""

    class Meta:
        model = BgpPeering
        fields = [
            "site",
            "device",
            "local_as",
            "local_ip",
            "peer_name",
            "remote_as",
            "remote_ip",
            "description",
        ]


class BgpPeeringFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering BgpPeering instances."""

    q = forms.CharField(required=False, label="Search")

    site = forms.ModelChoiceField(
        queryset=Site.objects.all(), required=False, to_field_name="slug"
    )

    device = forms.ModelChoiceField(
        queryset=Device.objects.all(),
        to_field_name="name",
        required=False,
    )

    local_as = forms.IntegerField(
        required=False,
    )

    remote_as = forms.IntegerField(
        required=False,
    )

    peer_name = forms.CharField(
        required=False,
    )

    class Meta:
        model = BgpPeering
        fields = []
