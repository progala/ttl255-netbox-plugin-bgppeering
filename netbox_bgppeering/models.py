from django.db import models

from dcim.fields import ASNField
from extras.models import ChangeLoggedModel
from ipam.fields import IPAddressField

from utilities.querysets import RestrictedQuerySet


class BgpPeering(ChangeLoggedModel):
    site = models.ForeignKey(
        to="dcim.Site", on_delete=models.SET_NULL, blank=True, null=True
    )
    device = models.ForeignKey(to="dcim.Device", on_delete=models.PROTECT)
    local_ip = models.ForeignKey(to="ipam.IPAddress", on_delete=models.PROTECT)
    local_as = ASNField(help_text="32-bit ASN used locally")
    remote_ip = IPAddressField(help_text="IPv4 or IPv6 address (with mask)")
    remote_as = ASNField(help_text="32-bit ASN used by peer")
    peer_name = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=200, blank=True)

    objects = RestrictedQuerySet.as_manager()
