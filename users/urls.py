from django.urls import path
from . import views


urlpatterns = [
    # ... other url patterns ...
    path("profile/", views.profile, name="profile"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
