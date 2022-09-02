from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index, name="index" ),
    path("login/", views.login_views , name="login"),
    path("logout/", views.logout_views , name="logout"),
    path("register/", views.register , name="register"),
    path("add_property/", views.add_property , name="add_property"),
    path("delete_property/<str:content>", views.delete_property , name="delete_property"),
    path("add_game/", views.add_game , name="add_game" ),
    path("delete_game/", views.delete_game , name="delete_game")
]