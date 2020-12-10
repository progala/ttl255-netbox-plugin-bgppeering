from django.contrib import admin
from .models import BgpPeering


@admin.register(BgpPeering)
class BgpPeeringAdmin(admin.ModelAdmin):
    list_display = ("device", "peer_name", "remote_as", "remote_ip")
