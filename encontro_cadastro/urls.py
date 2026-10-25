from django.contrib import admin
from django.urls import path
import cadastro.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", cadastro.views.home, name="home"),
]
