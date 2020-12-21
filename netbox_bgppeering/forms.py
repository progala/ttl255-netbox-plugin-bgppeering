from django import forms

from .models import BgpPeering


class BgpPeeringForm(forms.ModelForm):
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
