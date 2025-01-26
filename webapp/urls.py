from django.urls import include, path
from .views import api_views_standard, views, htmx_views
# For css and js
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

#####################################################
# API URL Configuration
#####################################################
# DB MODELS
router = routers.DefaultRouter()
router.register(r'users', api_views_standard.UserViewSet)
router.register(r'groups', api_views_standard.GroupViewSet)
router.register(r'ActionMap', api_views_standard.ActionMapViewSet)
router.register(r'CoachStates', api_views_standard.CoachStatesViewSet)
router.register(r'Coaches', api_views_standard.CoachesViewSet)
router.register(r'Games', api_views_standard.GamesViewSet)
router.register(r'PlayActions', api_views_standard.PlayActionsViewSet)
router.register(r'PlayLoadErrors', api_views_standard.PlayLoadErrorsViewSet)
router.register(r'PlayerGameHalfStats', api_views_standard.PlayerGameHalfStatsViewSet)
router.register(r'PlayerGameQuarterStats', api_views_standard.PlayerGameQuarterStatsViewSet)
router.register(r'PlayerGameStats', api_views_standard.PlayerGameStatsViewSet)
router.register(r'PlayerStates', api_views_standard.PlayerStatesViewSet)
router.register(r'Players', api_views_standard.PlayersViewSet)
router.register(r'Plays', api_views_standard.PlaysViewSet)
router.register(r'Seasons', api_views_standard.SeasonsViewSet)
router.register(r'TeamGameHalfStats', api_views_standard.TeamGameHalfStatsViewSet)
router.register(r'TeamGameQuarterStats', api_views_standard.TeamGameQuarterStatsViewSet)
router.register(r'TeamGameStats', api_views_standard.TeamGameStatsViewSet)
router.register(r'Teams', api_views_standard.TeamsViewSet)


urlpatterns = [
    path('', views.home),
    
    ###############################
    # API
    ###############################
    # Api Auth
    path(f'api/v{settings.API_VERSION}/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(f'api/v{settings.API_VERSION}/', include(router.urls)),
    path(f'api/v{settings.API_VERSION}/generic/<str:stat_model>/', api_views_standard.datatables_view),
    path(f'api/v{settings.API_VERSION}/generic/<str:stat_model>/columns/', api_views_standard.datatables_schemas_view),

    ###############################
    # HTMX
    ###############################
    path(f'htmx/', htmx_views.htmx),
]