from django.urls import path
from .views import PointsAPIView

urlpatterns = [
    path('closest_pair_api/', PointsAPIView.as_view(), name='points-api'),
]
