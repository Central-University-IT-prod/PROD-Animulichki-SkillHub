from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from api.teams.models import Team
from api.users.models import User

from api.teams.serializers import TeamSerializer


class AddUserToTeam(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, team_id, user_id):  # noqa: ARG002
        try:
            team = Team.objects.get(id=team_id)
            user = User.objects.get(id=user_id) # noqa
        except Team.DoesNotExist:
            return Response(
                {"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        team_serializer = TeamSerializer(team)
        return Response(team_serializer.data, status=status.HTTP_200_OK)


class AddTeam(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if "avatar" in request.FILES:
            serializer.initial_data["avatar"] = request.FILES["avatar"]
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowTeam(APIView):
    def get(self, request, team_id):  # noqa: ARG002
        team = get_object_or_404(
            Team,
            id=team_id,
        )
        serializer = TeamSerializer(
            instance=team,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowListTeam(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        teams = Team.objects.all()
        return teams
