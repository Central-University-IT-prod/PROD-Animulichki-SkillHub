from rest_framework import serializers

from api.teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = Team
        fields = "__all__"

    def validate(self, data):
        if not data.get("count_of_members"):
            msg = "Count of members is required"
            raise serializers.ValidationError(msg)
        if len(data.get("vacancies")) > data.get("count_of_members"):
            msg = "You already have a full team"
            raise serializers.ValidationError(msg)
        if len(data.get("vacancies")) == 0:
            msg = "Need at least one vacancy"
            raise serializers.ValidationError(msg)
        return data
