from django.urls import path

from .views import BusView, BusDeleteView


urlpatterns = [
    path("bus/", BusView.as_view(), name="bus"),
    path("bus/<int:id>/", BusDeleteView.as_view(), name="bus")
]

