from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()


def get_model_fields(model_class):
    base_attrs = dir(models.Model)
    model_fields = [
        field.name
        for field in model_class._meta.get_fields()
        if field.name not in base_attrs
        and not field.name.startswith("_")
        and field.name != "Meta"
    ]
    return model_fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


#########################################################
# DB MODELS SERIALIZERS
#########################################################
class ActionMapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionMap
        fields = get_model_fields(ActionMap)


class PlayMapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayMap
        fields = get_model_fields(PlayMap)


class CoachStatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoachStates
        fields = get_model_fields(CoachStates)


class CoachesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coaches
        fields = get_model_fields(Coaches)


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = get_model_fields(Games)


class PlayActionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayActions
        fields = get_model_fields(PlayActions)


class PlayLoadErrorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayLoadErrors
        fields = get_model_fields(PlayLoadErrors)


class PlayerGameHalfStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerGameHalfStats
        fields = get_model_fields(PlayerGameHalfStats)


class PlayerGameQuarterStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerGameQuarterStats
        fields = get_model_fields(PlayerGameQuarterStats)


class PlayerGameOvertimeStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerGameOvertimeStats
        fields = get_model_fields(PlayerGameOvertimeStats)


class PlayerGameStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerGameStats
        fields = get_model_fields(PlayerGameStats)


class PlayerStatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerStates
        fields = get_model_fields(PlayerStates)


class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Players
        fields = get_model_fields(Players)


class PlaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plays
        fields = get_model_fields(Plays)


class SeasonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seasons
        fields = get_model_fields(Seasons)


class TeamGameHalfStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamGameHalfStats
        fields = get_model_fields(TeamGameHalfStats)


class TeamGameQuarterStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamGameQuarterStats
        fields = get_model_fields(TeamGameQuarterStats)


class TeamGameOvertimeStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamGameOvertimeStats
        fields = get_model_fields(TeamGameOvertimeStats)


class TeamGameStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamGameStats
        fields = get_model_fields(TeamGameStats)


class TeamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teams
        fields = get_model_fields(Teams)
