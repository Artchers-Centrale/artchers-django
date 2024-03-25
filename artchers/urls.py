from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vote", views.page_vote, name="vote"),
    path('one_time_link/<str:access_code>', views.one_time_link, name='one_time_link'),
    path("cgu", views.cgu, name="cgu"),
    path("game", views.game, name="game"),
]