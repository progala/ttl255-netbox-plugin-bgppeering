from django.http import HttpResponse
from django.urls import path


def dummy_view(request):
    html = "<html><body>BGP Peering plugin.</body></html>"
    return HttpResponse(html)


urlpatterns = [
    path("", dummy_view, name="bgppeering_list"),
]
