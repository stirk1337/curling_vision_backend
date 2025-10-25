from django.urls import path
from .views import DetectAPIView, RotationAPIView, TrackAPIView, SummaryAPIView

urlpatterns = [
    path("detect/", DetectAPIView.as_view(), name="detect"),
    path("rotation/", RotationAPIView.as_view(), name="rotation"),
    path("track/", TrackAPIView.as_view(), name="track"),
    path("summary/", SummaryAPIView.as_view(), name="summary"),
]
