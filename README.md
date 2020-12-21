# NetBox BGP Peering Plugin

This repository contains source code of NetBox BGP Peering plugin.

There are multiple branches in this repository. Each branch represents different stage of the development of the plugin. These stages are describred in detail in Developing NetBox plugin tutorial @ ttl255.com.

This plugin is currently undergoing development and should not be used in production.

# Branches

| Name | Description | Tutorial part |
| --- | --- | --- |
| initial-plugin | Dev environment setup and plugin config | [^Part 1] |
| minimal-plugin | Minimal interactive plugin | [^Part 1]|
| adding-model | Adds model and exposes it in admin panel | [^Part 1] |
| model-migrations | Adds Django model migrations | [^Part 1] |
| bgppeering-view-init | Adds web UI page for displaying details of single object | [^Part 2] |
| bgppeering-list-view-init | Adds web UI page for displaying list of objects | [^Part 2] |
| bgppeering-create-view-init | Adds web UI page with form for creating objects | [^Part 2] |

\
Follow the below links to the tutorial if you'd like to see in details how I built this plugin:

[Developing NetBox Plugin - Part 1 - Setup and initial build](https://ttl255.com/developing-netbox-plugin-part-1-setup-and-initial-build/)

[Developing NetBox Plugin - Part 2 - Adding web UI pages](https://ttl255.com/developing-netbox-plugin-part-2-adding-ui-pages/)


[^Part 1]: https://ttl255.com/developing-netbox-plugin-part-1-setup-and-initial-build/
[^Part 2]: https://ttl255.com/developing-netbox-plugin-part-2-adding-ui-pages/