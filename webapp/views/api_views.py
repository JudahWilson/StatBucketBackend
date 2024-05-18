from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import *
from ..models import *
from django_filters import rest_framework as filters
from ..filters import *

#########################################################
# Generic search any model
#########################################################
@api_view(['GET'])
def datatables_view(request, stat_model):
    if request.method == 'GET':
        """
        @object - one of the models where that API View set is defined for them
        """
        
        # if user searched for an existing model
        if stat_model in get_model_names():

            # Get the api endpoint associated to the user-provided model name
            view_set_class = globals().get(stat_model + 'ViewSet')
            return Response(data=view_set_class.as_view({'get': 'list'})(request._request).data, status=status.HTTP_200_OK)

#######################################################
# Generic search any schema
#######################################################
@api_view(['GET'])
def datatables_schemas_view(request, stat_model):
    if request.method == 'GET':
        """
        @object - one of the models where that API View set is defined for them
        """
        # if user searched for an existing model
        # TODO can i define for the openapi docs that the input is limited to the names it is limited to?
        # TODO serialize + validate the input schema as well (seems to be supported)
        if stat_model in get_model_names():
            data = request.data

            # Get the model class associated to the user-provided model name
            model_class = globals().get(stat_model)
            columns = get_model_fields(model_class=model_class)
            response_data = []
            for col in columns:
                response_data.append({'data': col, 'title': ' '.join(word.capitalize() for word in col.split('_'))})
            return Response(data=response_data, status=status.HTTP_200_OK)

#########################################################
#region All MODELS VIEWSETS
#########################################################
# Parent viewset class that all other viewsets inherit from
class InternalAPIViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter
        
        # order_by and desc
        order_by = self.request.query_params.get('order_by')            
        if order_by:
            if self.request.query_params.get('order[0][column]') == 'desc':
                order_by = '-' + order_by
            queryset = queryset.order_by(order_by)

        

        return queryset
class UserViewSet(InternalAPIViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
class GroupViewSet(InternalAPIViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


ActionMapFilter = UniversalFilter.create_filter(ActionMap)
class ActionMapViewSet(InternalAPIViewSet):
    queryset = ActionMap.objects.all()
    serializer_class = ActionMapSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ActionMapFilter


CoachStatesFilter = UniversalFilter.create_filter(CoachStates)
class CoachStatesViewSet(InternalAPIViewSet):
    queryset = CoachStates.objects.all()
    serializer_class = CoachStatesSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CoachStatesFilter


CoachesFilter = UniversalFilter.create_filter(Coaches)
class CoachesViewSet(InternalAPIViewSet):
    queryset = Coaches.objects.all()
    serializer_class = CoachesSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CoachesFilter


GamesFilter = UniversalFilter.create_filter(Games)
class GamesViewSet(InternalAPIViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GamesFilter


PlayActionsFilter = UniversalFilter.create_filter(PlayActions)
class PlayActionsViewSet(InternalAPIViewSet):
    queryset = PlayActions.objects.all()
    serializer_class = PlayActionsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayActionsFilter


PlayLoadErrorsFilter = UniversalFilter.create_filter(PlayLoadErrors)
class PlayLoadErrorsViewSet(InternalAPIViewSet):
    queryset = PlayLoadErrors.objects.all()
    serializer_class = PlayLoadErrorsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayLoadErrorsFilter


PlayerGameHalfStatsFilter = UniversalFilter.create_filter(PlayerGameHalfStats)
class PlayerGameHalfStatsViewSet(InternalAPIViewSet):
    queryset = PlayerGameHalfStats.objects.all()
    serializer_class = PlayerGameHalfStatsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayerGameHalfStatsFilter


PlayerGameQuarterStatsFilter = UniversalFilter.create_filter(PlayerGameQuarterStats)
class PlayerGameQuarterStatsViewSet(InternalAPIViewSet):
    queryset = PlayerGameQuarterStats.objects.all()
    serializer_class = PlayerGameQuarterStatsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayerGameQuarterStatsFilter


PlayerGameStatsFilter = UniversalFilter.create_filter(PlayerGameStats)
class PlayerGameStatsViewSet(InternalAPIViewSet):
    queryset = PlayerGameStats.objects.all()
    serializer_class = PlayerGameStatsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayerGameStatsFilter


PlayerStatesFilter = UniversalFilter.create_filter(PlayerStates)
class PlayerStatesViewSet(InternalAPIViewSet):
    queryset = PlayerStates.objects.all()
    serializer_class = PlayerStatesSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayerStatesFilter


PlayersFilter = UniversalFilter.create_filter(Players)
class PlayersViewSet(InternalAPIViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlayersFilter


PlaysFilter = UniversalFilter.create_filter(Plays)
class PlaysViewSet(InternalAPIViewSet):
    queryset = Plays.objects.all()
    serializer_class = PlaysSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaysFilter


SeasonsFilter = UniversalFilter.create_filter(Seasons)
class SeasonsViewSet(InternalAPIViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SeasonsFilter


TeamGameHalfStatsFilter = UniversalFilter.create_filter(TeamGameHalfStats)
class TeamGameHalfStatsViewSet(InternalAPIViewSet):
    queryset = TeamGameHalfStats.objects.all()
    serializer_class = TeamGameHalfStatsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeamGameHalfStatsFilter


TeamGameQuarterStatsFilter = UniversalFilter.create_filter(TeamGameQuarterStats)
class TeamGameQuarterStatsViewSet(InternalAPIViewSet):
    queryset = TeamGameQuarterStats.objects.all()
    serializer_class = TeamGameQuarterStatsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeamGameQuarterStatsFilter


TeamGameStatsFilter = UniversalFilter.create_filter(TeamGameStats)
class TeamGameStatsViewSet(InternalAPIViewSet):
    queryset = TeamGameStats.objects.all()
    serializer_class = TeamGameStatsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeamGameStatsFilter


TeamsFilter = UniversalFilter.create_filter(Teams)
class TeamsViewSet(InternalAPIViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeamsFilter
#endregion
