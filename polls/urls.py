from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<int:question_id>/detail/", views.detail, name="detail"),
    path("specifics/<int:question_id>/vote/", views.vote, name="vote"),
    path("specifics/<int:question_id>/results/", views.results, name="results"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
