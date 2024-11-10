from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<int:question_id>/detail/", views.detail, name="detail"),
    path("specifics/<int:question_id>/vote/", views.vote, name="vote"),
    path("specifics/<int:question_id>/results/", views.results, name="results"),
]
