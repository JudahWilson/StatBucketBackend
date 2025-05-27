# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_model_names():
    """
    Get a list of all models' names as a strings
    """
    import inspect
    class_names = []
    for name, obj in inspect.getmembers(inspect.getmodule(get_model_names)):
        if inspect.isclass(obj) and obj.__module__ == get_model_names.__module__:
            class_names.append(name)
    return class_names


##########################################
# CUSTOM USER MODEL
##########################################
class WebUser(AbstractUser):
    pass

    # add additional fields in here

    def __str__(self):
        return self.username
    
##########################################
# StatBucket MODELS
##########################################
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class ActionMap(models.Model):
    description = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.description
    
    class Meta:
        managed = False
        db_table = 'ActionMap'
        verbose_name_plural = 'Action Map'

class CoachStates(models.Model):
    coach_br_id = models.CharField(max_length=10, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        # coach and start date to end date
        return self.coach_br_id + ' ' + self.start_date.strftime("%Y-%m-%d %H:%M:%S") + ' to ' + self.end_date.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        managed = False
        db_table = 'CoachStates'
        verbose_name_plural = 'Coach States'


class Coaches(models.Model):
    br_id = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=35, blank=True, null=True)
    last_name = models.CharField(max_length=35, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    origin_city = models.CharField(max_length=35, blank=True, null=True)
    origin_territory = models.CharField(max_length=35, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        managed = False
        db_table = 'Coaches'
        verbose_name_plural = 'Coaches'

class Games(models.Model):
    br_id = models.CharField(max_length=12, blank=True, null=True)
    season_br_id = models.CharField(max_length=8, blank=True, null=True)
    home_team_br_id = models.CharField(max_length=3, blank=True, null=True)
    away_team_br_id = models.CharField(max_length=3, blank=True, null=True)
    home_team_points = models.IntegerField(blank=True, null=True)
    away_team_points = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    arena = models.CharField(max_length=65, blank=True, null=True)
    ot = models.CharField(max_length=3, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    inactive_players = models.TextField(blank=True, null=True)
    officials = models.TextField(blank=True, null=True)
    game_duration = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Games'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S") + ' - ' + self.home_team_br_id + ' vs ' + self.away_team_br_id

class PlayActions(models.Model):
    play_id = models.IntegerField(blank=True, null=True)
    player_br_id = models.CharField(max_length=9, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=60,blank=True, null=True)

    def __str__(self):
        return self.play_id + ' - ' + self.player_br_id + ' - ' + self.action_id

    class Meta:
        managed = False
        db_table = 'PlayActions'
        verbose_name_plural = 'Play Actions'


class PlayLoadErrors(models.Model):
    url = models.CharField(max_length=200, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=7, blank=True, null=True)
    html = models.CharField(max_length=300, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    is_play_not_yet_supported_error = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.url + ' - ' + self.time
    
    class Meta:
        managed = False
        db_table = 'PlayLoadErrors'
        verbose_name_plural = 'Play Load Errors'


class PlayerGameHalfStats(models.Model):
    player_br_id = models.CharField(max_length=9, blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    opponent_br_id = models.CharField(max_length=3, blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    seconds_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.player_br_id + ' - ' + self.game_br_id
    
    class Meta:
        managed = False
        db_table = 'PlayerGameHalfStats'
        verbose_name_plural = 'Player Game Half Stats'


class PlayerGameQuarterStats(models.Model):
    player_br_id = models.CharField(max_length=9, blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    opponent_br_id = models.CharField(max_length=3, blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    seconds_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.player_br_id + ' - ' + self.game_br_id
    
    class Meta:
        managed = False
        db_table = 'PlayerGameQuarterStats'
        verbose_name_plural = 'Player Game Quarter Stats'
        
class PlayerGameOvertimeStats(models.Model):
    player_br_id = models.CharField(max_length=9, blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    opponent_br_id = models.CharField(max_length=3, blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)
    seconds_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.player_br_id + ' - ' + self.game_br_id + ' - ' + self.overtime
    
    class Meta:
        managed = False
        db_table = 'PlayerGameOvertimeStats'
        verbose_name_plural = 'Player Game Overtime Stats'


class PlayerGameStats(models.Model):
    player_br_id = models.CharField(max_length=9, blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    opponent_team_br_id = models.CharField(max_length=3, blank=True, null=True)
    played = models.IntegerField(blank=True, null=True)
    reason_for_absence = models.CharField(max_length=20, blank=True, null=True)
    started = models.IntegerField(blank=True, null=True)
    seconds_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)
    true_shooting_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    effective_field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    three_point_attempt_rate = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    free_throw_attempt_rate = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    offensive_rebound_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    defensive_rebound_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    total_rebound_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    assist_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    steal_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    block_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    turnover_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    usage_percentage = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    offensive_rating = models.IntegerField(blank=True, null=True)
    defensive_rating = models.IntegerField(blank=True, null=True)
    box_plus_minus = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return self.player_br_id + ' - ' + self.game_br_id
    
    class Meta:
        managed = False
        db_table = 'PlayerGameStats'
        verbose_name_plural = 'Player Game Stats'


class PlayerStates(models.Model):
    player_br_id = models.CharField(max_length=9, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    jersey_no = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=3, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.player_br_id + ' - ' + self.start_date.strftime("%Y-%m-%d %H:%M:%S") + ' to ' + self.end_date.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        managed = False
        db_table = 'PlayerStates'
        verbose_name_plural = 'Player States'


class Players(models.Model):
    br_id = models.CharField(max_length=9, blank=True, null=True, db_comment='TEST')
    first_name = models.CharField(max_length=35, blank=True, null=True)
    last_name = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    territory = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=5, blank=True, null=True)
    year_start = models.CharField(max_length=4, blank=True, null=True)
    year_end = models.CharField(max_length=4, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    height_str = models.CharField(max_length=4, blank=True, null=True)
    height_in = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    colleges = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        managed = False
        db_table = 'Players'
        verbose_name_plural = 'Players'


class Plays(models.Model):
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    clock_time = models.CharField(max_length=7, blank=True, null=True)
    distance_feet = models.IntegerField(blank=True, null=True)
    home_score: int
    away_score: int

    class Meta:
        managed = False
        db_table = 'Plays'
        verbose_name_plural = 'Plays'


class Seasons(models.Model):
    season_start_year = models.CharField(max_length=4, blank=True, null=True)
    season_end_year = models.CharField(max_length=4, blank=True, null=True)
    league = models.CharField(max_length=3, blank=True, null=True)
    champion = models.IntegerField(blank=True, null=True)
    mvp = models.IntegerField(blank=True, null=True)
    roy = models.IntegerField(blank=True, null=True)
    scoring_leader = models.IntegerField(blank=True, null=True)
    rebounds_leader = models.IntegerField(blank=True, null=True)
    assists_leader = models.IntegerField(blank=True, null=True)
    win_shares_leader = models.IntegerField(blank=True, null=True)
    br_id = models.CharField(max_length=8, blank=True, null=True)
    active = models.CharField(max_length=8, blank=True, null=True)
    champion_br_id = models.CharField(max_length=20, blank=True, null=True)
    mvp_br_id = models.CharField(max_length=20, blank=True, null=True)
    roy_br_id = models.CharField(max_length=20, blank=True, null=True)
    scoring_leader_br_id = models.CharField(max_length=20, blank=True, null=True)
    rebounding_leader_br_id = models.CharField(max_length=20, blank=True, null=True)
    assists_leader_br_id = models.CharField(max_length=20, blank=True, null=True)
    winshares_leader_br_id = models.CharField(max_length=20, blank=True, null=True)
    scoring_leader_points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.season_start_year + ' - ' + self.season_end_year
    
    class Meta:
        managed = False
        db_table = 'Seasons'
        verbose_name_plural = 'Seasons'


class TeamGameHalfStats(models.Model):
    game_id = models.IntegerField(blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    half = models.IntegerField(blank=True, null=True)
    minutes_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.game_id + ' - ' + self.half
    
    class Meta:
        managed = False
        db_table = 'TeamGameHalfStats'
        verbose_name_plural = 'Team Game Half Stats'

class TeamGameQuarterStats(models.Model):
    game_id = models.IntegerField(blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    minutes_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.game_id + ' - ' + self.quarter
    
    class Meta:
        managed = False
        db_table = 'TeamGameQuarterStats'
        verbose_name_plural = 'Team Game Quarter Stats'
        
class TeamGameOvertimeStats(models.Model):
    game_id = models.IntegerField(blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)
    minutes_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.game_id + ' - ' + self.overtime
    
    class Meta:
        managed = False
        db_table = 'TeamGameOvertimeStats'
        verbose_name_plural = 'Team Game Overtime Stats'

class TeamGameStats(models.Model):
    game_id = models.IntegerField(blank=True, null=True)
    game_br_id = models.CharField(max_length=12, blank=True, null=True)
    team_br_id = models.CharField(max_length=3, blank=True, null=True)
    minutes_played = models.IntegerField(blank=True, null=True)
    field_goals = models.IntegerField(blank=True, null=True)
    field_goal_attempts = models.IntegerField(blank=True, null=True)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    three_pointers = models.IntegerField(blank=True, null=True)
    three_pointer_attempts = models.IntegerField(blank=True, null=True)
    three_pointer_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    free_throws = models.IntegerField(blank=True, null=True)
    free_throw_attempts = models.IntegerField(blank=True, null=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    personal_fouls = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    true_shooting_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    effective_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    three_point_attempt_rate = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    free_throw_attempt_rate = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    offensive_rebound_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    defensive_rebound_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_rebound_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    assist_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    steal_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    block_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turnover_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    usage_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    offensive_rating = models.IntegerField(blank=True, null=True)
    defensive_rating = models.IntegerField(blank=True, null=True)
    pace_factor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    ft_per_fga = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    inactive_players = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.game_id + ' - ' + self.home_team_id + ' vs ' + self.opponent_team_id
    
    class Meta:
        managed = False
        db_table = 'TeamGameStats'
        verbose_name_plural = 'Team Game Stats'

class Teams(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    br_id = models.CharField(max_length=3, blank=True, null=True)
    league = models.CharField(max_length=3, blank=True, null=True)
    season_start_year = models.CharField(max_length=4, blank=True, null=True)
    season_end_year = models.CharField(max_length=4, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.season_start_year + ' to ' + self.season_end_year
    
    class Meta:
        managed = False
        db_table = 'Teams'
        verbose_name_plural = 'Teams'