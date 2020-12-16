from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:netbox_bgppeering:bgppeering_list",
        link_text="BGP Peerings",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_bgppeering:bgppeering_add",
                title="Add",
                icon_class="fa fa-plus",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
