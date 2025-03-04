from django.urls import path
from .views import post_comment_create_add_list_view

urlpatterns = [
    path('', post_comment_create_add_list_view, name='main-post-view')
]
