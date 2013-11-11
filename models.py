from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging

# class Game(ndb.Model):
#     date = ndb.DateProperty(required=True)
#     player_faction = ndb.StringProperty(required=True)
#     player_warcaster = ndb.StringProperty(required=True)
#     opponent_name = ndb.StringProperty()
#     opponent_faction = ndb.StringProperty(required=True)
#     opponent_warcaster = ndb.StringProperty(required=True)
#     size = ndb.IntegerProperty()
#     result = ndb.StringProperty(required=True)
#     won = ndb.BooleanProperty()
#     draw = ndb.BooleanProperty()
#     teaching = ndb.BooleanProperty()

class Combatant(ndb.Model):
    player = ndb.KeyProperty(kind=Player, indexed=True, required=True)
    # Integer value is index into factions constant.
    faction = ndb.IntegerProperty(indexed=True,required=True)
    # Integer value is index into casters constant sub-list of factions.
    caster = ndb.IntegerProperty(indexed=True, required=True)


class Game(ndb.Model):
    player_1 = ndb.StructuredProperty(Combatant, indexed=True, required=True)
    player_2 = ndb.StructuredProperty(Combatant, indexed=True, required=True)
    # 0 = Tied, 1 = Player 1 Victory, 2 = Player 2 Victory
    result = ndb.IntegerProperty(indexed=True, required=True)
    size = ndb.IntegerProperty(indexed=False, required=True)
    # Integer index into the list of outcome constants.
    result = ndb.IntegerProperty(indexed=True)
    date = ndb.DateProperty(indexed=True, required=True)
    teaching = ndb.BooleanProperty(indexed=False)


class Player(ndb.Model):
    name = ndb.StringProperty(required=True, indexed=True)
    user = ndb.UserProperty(indexed=True)
    #TODO Anything else to track.