from django.urls import path
from . import views

app_name = "anketler"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # Generic Views 'soru_id' yerine 'pk' (Primary Key) ismi bekler.
    path("<int:pk>/", views.DetayView.as_view(), name="detay"),
    path("<int:pk>/sonuclar/", views.SonuclarView.as_view(), name="sonuclar"),
    path("<int:soru_id>/oy_ver/", views.oy_ver, name="oy_ver"),
]