from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
] 