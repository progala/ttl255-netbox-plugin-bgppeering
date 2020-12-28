from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

from .icon_classes import icon_classes


menu_items = (
    PluginMenuItem(
        link="plugins:netbox_bgppeering:bgppeering_list",
        link_text="BGP Peerings",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_bgppeering:bgppeering_add",
                title="Add",
                icon_class=icon_classes.get("plus"),
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
