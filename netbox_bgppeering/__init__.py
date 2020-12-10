from extras.plugins import PluginConfig


class BgpPeering(PluginConfig):
    name = "netbox_bgppeering"
    verbose_name = "BGP Peering"
    description = "Manages BGP peer connections"
    version = "0.1"
    author = "Przemek Rogala <ttl255.com>"
    author_email = "pr@ttl255.com"
    base_url = "bgp-peering"
    min_version = "2.9"
    required_settings = []
    default_settings = {}


config = BgpPeering
