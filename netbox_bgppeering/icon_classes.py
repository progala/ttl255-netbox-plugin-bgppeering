from .release import NETBOX_RELEASE_CURRENT, NETBOX_RELEASE_210


if NETBOX_RELEASE_CURRENT >= NETBOX_RELEASE_210:
    icon_classes = {
        "plus": "mdi mdi-plus-thick",
        "search": "mdi mdi-magnify",
        "remove": "mdi mdi-close-thick",
        "trash": "mdi mdi-trash-can-outline",
        "pencil": "mdi mdi-pencil",
    }
else:
    icon_classes = {
        "plus": "fa fa-plus",
        "search": "fa fa-search",
        "remove": "fa fa-remove",
        "trash": "fa fa-trash",
        "pencil": "fa fa-pencil",
    }
