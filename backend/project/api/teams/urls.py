from django.urls import path

from api.teams import views

app_name = "teams"

urlpatterns = [
    path(
        "/add_user/<int:team_id>/<int:user_id>",
        views.AddUserToTeam.as_view(),
        name="add_user_to_team",
    ),
    path(
        "/add",
        views.AddTeam.as_view(),
        name="add_team",
    ),
    path(
        "/<int:team_id>",
        views.ShowTeam.as_view(),
        name="show_team",
    ),
    path(
        "",
        views.ShowListTeam.as_view(),
        name="show_list_teams",
    ),
]
