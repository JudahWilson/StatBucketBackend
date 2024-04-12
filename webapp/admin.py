from django.contrib import admin
from webapp.models import *

# Register your models here.
admin.site.site_header = 'StatBucket Admin'
admin.site.site_title = 'StatBucket Admin'
admin.site.index_title = 'StatBucket Admin'

# admin.site.register(Games)
admin.site.register(WebUser)
admin.site.register(ActionMap)
admin.site.register(CoachStates)
admin.site.register(Coaches)
admin.site.register(Games)
admin.site.register(PlayActions)
admin.site.register(PlayLoadErrors)
admin.site.register(PlayerGameHalfStats)
admin.site.register(PlayerGameQuarterStats)
admin.site.register(PlayerGameStats)
admin.site.register(PlayerStates)
admin.site.register(Players)
admin.site.register(Plays)
admin.site.register(Seasons)
admin.site.register(TeamGameHalfStats)
admin.site.register(TeamGameQuarterStats)
admin.site.register(TeamGameStats)
admin.site.register(Teams)