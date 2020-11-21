from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("ycy", views.ycy, name="ycy"),
    path("<str:name>", views.greet, name="greet")
]