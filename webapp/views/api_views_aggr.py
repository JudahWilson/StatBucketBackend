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
def aggr_view(request):
    if request.method == 'GET':
        '''
        over 50 pts for player of game
        teams with no championships
        avg ppg per team of season X
        pie chart of rebounds of game
        points of last 100 games of team
        avg points per month per last 12 months
        scatterplot of 150 point games all time
        dynamically add teams or instance of whatever subject to same graph!
        click chart element to describe its subject's details? 
        mysql query to get all fk relationships for ease of establishing relationships over rest api
        '''