from django.urls import include, path

urlpatterns = [
    path("ping", include("api.ping.urls")),
    path("auth", include("api.users.urls")),
    path("teams", include("api.teams.urls")),
]
