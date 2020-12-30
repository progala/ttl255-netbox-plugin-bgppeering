from django.http import HttpResponse
from django.urls import path

from .views import (
    BgpPeeringCreateView,
    BgpPeeringDeleteView,
    BgpPeeringListView,
    BgpPeeringView,
)


urlpatterns = [
    path("", BgpPeeringListView.as_view(), name="bgppeering_list"),
    path("<int:pk>/", BgpPeeringView.as_view(), name="bgppeering"),
    path("add/", BgpPeeringCreateView.as_view(), name="bgppeering_add"),
    path("<int:pk>/delete/", BgpPeeringDeleteView.as_view(), name="bgppeering_delete"),
]
