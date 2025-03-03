from django.urls import path
from .views import myprofile_view

urlpatterns = [
    path('myprofile', myprofile_view, name="myprofile-view")
]
