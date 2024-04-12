from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import *
from ..models import *


#########################################################
# DataTables APIs
#########################################################
@api_view(['GET'])
def datatables_view(request, stat_model):
    if request.method == 'GET':
        """
        @object - one of the models where that API View set is defined for them
        """
        
        order_by = request.query_params.get('order_by')
        desc = request.query_params.get('desc')
        search_value = request.query_params.get('search')
        
        # if user searched for an existing model
        # TODO can i define for the openapi docs that the input is limited to the names it is limited to?
        if stat_model in get_model_names():
            data = request.data

            # Get the api endpoint associated to the user-provided model name
            view_set_class = globals().get(stat_model + 'ViewSet')
            # TODO customize things like order by and search by column and search all
            # TODO serialize + validate the input schema as well (seems to be supported)
            # queryset = cls.objects.all()
            # Get the model class' associated serializer
            # serializer_class = globals().get(object + 'Serializer')
            # permission_classes = [permissions.AllowAny]

            # TODO how exactly do i return data in the same way my other "view sets" are doing it?
            return Response(data=view_set_class.as_view({'get': 'list'})(request._request).data, status=status.HTTP_200_OK)

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
# DB MODELS VIEWSETS
#########################################################
# Parent viewset class that all other viewsets inherit from
class InternalAPIViewSet(viewsets.ModelViewSet):
        def get_queryset(self):
            queryset = super().get_queryset()

            order_by = self.request.query_params.get('order_by')
            if self.request.query_params.get('desc') == 'true':
                order_by = '-' + order_by
                
            if order_by:
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

class ActionMapViewSet(InternalAPIViewSet):
    queryset = ActionMap.objects.all()
    serializer_class = ActionMapSerializer
    permission_classes = [permissions.AllowAny]
class CoachStatesViewSet(InternalAPIViewSet):
    queryset = CoachStates.objects.all()
    serializer_class = CoachStatesSerializer
    permission_classes = [permissions.AllowAny]
class CoachesViewSet(InternalAPIViewSet):
    queryset = Coaches.objects.all()
    serializer_class = CoachesSerializer
    permission_classes = [permissions.AllowAny]
class GamesViewSet(InternalAPIViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = [permissions.AllowAny]
        
class PlayActionsViewSet(InternalAPIViewSet):
    queryset = PlayActions.objects.all()
    serializer_class = PlayActionsSerializer
    permission_classes = [permissions.AllowAny]
class PlayLoadErrorsViewSet(InternalAPIViewSet):
    queryset = PlayLoadErrors.objects.all()
    serializer_class = PlayLoadErrorsSerializer
    permission_classes = [permissions.AllowAny]
class PlayerGameHalfStatsViewSet(InternalAPIViewSet):
    queryset = PlayerGameHalfStats.objects.all()
    serializer_class = PlayerGameHalfStatsSerializer
    permission_classes = [permissions.AllowAny]
class PlayerGameQuarterStatsViewSet(InternalAPIViewSet):
    queryset = PlayerGameQuarterStats.objects.all()
    serializer_class = PlayerGameQuarterStatsSerializer
    permission_classes = [permissions.AllowAny]
class PlayerGameStatsViewSet(InternalAPIViewSet):
    queryset = PlayerGameStats.objects.all()
    serializer_class = PlayerGameStatsSerializer
    permission_classes = [permissions.AllowAny]
class PlayerStatesViewSet(InternalAPIViewSet):
    queryset = PlayerStates.objects.all()
    serializer_class = PlayerStatesSerializer
    permission_classes = [permissions.AllowAny]
class PlayersViewSet(InternalAPIViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = [permissions.AllowAny]
class PlaysViewSet(InternalAPIViewSet):
    queryset = Plays.objects.all()
    serializer_class = PlaysSerializer
    permission_classes = [permissions.AllowAny]
class SeasonsViewSet(InternalAPIViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [permissions.AllowAny]
class TeamGameHalfStatsViewSet(InternalAPIViewSet):
    queryset = TeamGameHalfStats.objects.all()
    serializer_class = TeamGameHalfStatsSerializer
    permission_classes = [permissions.AllowAny]
class TeamGameQuarterStatsViewSet(InternalAPIViewSet):
    queryset = TeamGameQuarterStats.objects.all()
    serializer_class = TeamGameQuarterStatsSerializer
    permission_classes = [permissions.AllowAny]
class TeamGameStatsViewSet(InternalAPIViewSet):
    queryset = TeamGameStats.objects.all()
    serializer_class = TeamGameStatsSerializer
    permission_classes = [permissions.AllowAny]
class TeamsViewSet(InternalAPIViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = [permissions.AllowAny]