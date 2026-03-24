from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("anketler/", include("anketler.urls")),
    path("admin/", admin.site.urls),
]
admin.site.site_header = "PANEL İŞTE "   
admin.site.site_title = "AYBOOOOO"             
admin.site.index_title = "ANKET İŞTE DOLDUR KAPAT"