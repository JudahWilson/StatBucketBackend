from django.urls import include, path
from .views import api_views, views, htmx_views
# For css and js
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

#####################################################
# API URL Configuration
#####################################################
# DB MODELS
router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'ActionMap', api_views.ActionMapViewSet)
router.register(r'CoachStates', api_views.CoachStatesViewSet)
router.register(r'Coaches', api_views.CoachesViewSet)
router.register(r'Games', api_views.GamesViewSet)
router.register(r'PlayActions', api_views.PlayActionsViewSet)
router.register(r'PlayLoadErrors', api_views.PlayLoadErrorsViewSet)
router.register(r'PlayerGameHalfStats', api_views.PlayerGameHalfStatsViewSet)
router.register(r'PlayerGameQuarterStats', api_views.PlayerGameQuarterStatsViewSet)
router.register(r'PlayerGameStats', api_views.PlayerGameStatsViewSet)
router.register(r'PlayerStates', api_views.PlayerStatesViewSet)
router.register(r'Players', api_views.PlayersViewSet)
router.register(r'Plays', api_views.PlaysViewSet)
router.register(r'Seasons', api_views.SeasonsViewSet)
router.register(r'TeamGameHalfStats', api_views.TeamGameHalfStatsViewSet)
router.register(r'TeamGameQuarterStats', api_views.TeamGameQuarterStatsViewSet)
router.register(r'TeamGameStats', api_views.TeamGameStatsViewSet)
router.register(r'Teams', api_views.TeamsViewSet)


urlpatterns = [
    path('', views.index),
    
    ###############################
    # API
    ###############################
    # Api Auth
    path(f'api/v{settings.API_VERSION}/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(f'api/v{settings.API_VERSION}/', include(router.urls)),
    path(f'api/v{settings.API_VERSION}/generic/<str:stat_model>/', api_views.datatables_view),
    path(f'api/v{settings.API_VERSION}/generic/<str:stat_model>/columns/', api_views.datatables_schemas_view),

    ###############################
    # HTMX
    ###############################
    path(f'htmx/', htmx_views.htmx),
]