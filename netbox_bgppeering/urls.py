from django.http import HttpResponse
from django.urls import path

from .views import BgpPeeringCreateView, BgpPeeringView, BgpPeeringListView


urlpatterns = [
    path("", BgpPeeringListView.as_view(), name="bgppeering_list"),
    path("<int:pk>/", BgpPeeringView.as_view(), name="bgppeering"),
    path("add/", BgpPeeringCreateView.as_view(), name="bgppeering_add"),
]
