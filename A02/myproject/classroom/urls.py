from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Define a list of URLs patterns
urlpatterns = [
    path('', views.index, name = 'index'),
    path("register/", views.register, name="register"),
    path("reserve/<int:room_id>", views.reserve_room, name="reserve_room"),
    path("cancel/", views.cancel_reservation, name="cancel_reservation"),
    path("login/", auth_views.LoginView.as_view(template_name="rooms/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]