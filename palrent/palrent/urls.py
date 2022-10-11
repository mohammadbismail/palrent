
from django.urls import path, include

urlpatterns = [
    path("", include("user_app.urls")),
    path("my_dashboard/", include("car_app.urls")),
]
