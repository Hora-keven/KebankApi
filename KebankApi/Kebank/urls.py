from django.urls import path
from Kebank.Api.viewsets import *

urlpatterns = [

    path('physicalperson/', PhysicalPersonViewSet.as_view({"post":"create", "get":"list"})),
    path('physicalperson/<int:pk>', PhysicalPersonViewSet.as_view({"get":"list"})),
    path('juridicperson/', JuridicPersonViewSet.as_view({"post":"create", "get":"list"})),
    path('account/', AccountViewSet.as_view({"post":"create", "get":"list"})),
    path("address/", AddressViewSet.as_view({"post":"create", "get":"list"})),
    path("card/", CardViewSet.as_view({"post":"create", "get":"list"})),
    path("loan/", LoanViewSet.as_view({"post":"create", "get":"list"})),
    path("card/<int:pk>", CardViewSet.as_view({"delete":"destroy", "get":"list"})),
    path("movimentation/", MovimentationViewSet.as_view({"get":"list"})),
    path("pix/", PixViewSet.as_view({"post":"create", "get":"list"})),
    path("investment/", InvestmentViewSet.as_view({"post":"create", "get":"list"})),
]