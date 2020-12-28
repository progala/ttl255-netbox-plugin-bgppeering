from .release import NETBOX_RELEASE_CURRENT, NETBOX_RELEASE_210


if NETBOX_RELEASE_CURRENT >= NETBOX_RELEASE_210:
    icon_classes = {
        "plus": "mdi mdi-plus-thick",
        "search": "mdi mdi-magnify",
        "remove": "mdi mdi-close-thick",
    }
else:
    icon_classes = {
        "plus": "fa fa-plus",
        "search": "fa fa-search",
        "remove": "fa fa-remove",
    }
