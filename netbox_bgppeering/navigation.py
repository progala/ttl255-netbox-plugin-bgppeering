from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

from .release import NETBOX_RELEASE_CURRENT, NETBOX_RELEASE_210


if NETBOX_RELEASE_CURRENT >= NETBOX_RELEASE_210:
    icon_class_plus = "mdi mdi-plus-thick"
else:
    icon_class_plus = "fa fa-plus"

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_bgppeering:bgppeering_list",
        link_text="BGP Peerings",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_bgppeering:bgppeering_add",
                title="Add",
                icon_class=icon_class_plus,
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
