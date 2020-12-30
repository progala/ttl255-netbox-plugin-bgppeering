import ipaddress

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

    def clean(self):
        cleaned_data = super().clean()
        local_ip = cleaned_data.get("local_ip")
        remote_ip = cleaned_data.get("remote_ip")

        if local_ip and remote_ip:
            # We can trust these are valid IP addresses. Format validation done in .super()
            if (
                ipaddress.ip_interface(str(local_ip)).network
                != ipaddress.ip_interface(str(remote_ip)).network
            ):
                msg = "Local IP and Remote IP must be in the same network."
                self.add_error("local_ip", msg)
                self.add_error("remote_ip", msg)


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
        label="Local ASN",
    )

    remote_as = forms.IntegerField(required=False, label="Remote ASN")

    peer_name = forms.CharField(
        required=False,
        label="Peer Name",
    )

    class Meta:
        model = BgpPeering
        fields = []
