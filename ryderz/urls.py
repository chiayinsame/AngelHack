from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("tutorsignup/", views.tutor_signup, name="tutor_signup")
]