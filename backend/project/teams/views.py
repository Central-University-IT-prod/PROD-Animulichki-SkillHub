from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from users.models import User

from teams.models import Team
from teams.serializers import TeamSerializer


class AddUserToTeam(APIView):
    def post(self, request, team_id, user_id):  # noqa: ARG002
        try:
            team = Team.objects.get(id=team_id)
            user = User.objects.get(id=user_id)
        except Team.DoesNotExist:
            return Response(
                {"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        team.members.add(user)
        team_serializer = TeamSerializer(team)
        return Response(team_serializer.data, status=status.HTTP_200_OK)


class TeamsViewSet(ModelViewSet):
    http_method_names = ("get",)

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]