import uuid
from typing import List
from trueskill import Rating, TrueSkill

ts_pmo = TrueSkill

# it seems we can calculate rating change based on rank
# STUB
class Player:
    def __init__(self, elo: int, uid: uuid.UUID):
        self.elo = Rating(elo)
        self.uid = uid

class Match:
    def __init__(self, participants_in_ranking: List[Player]):
        pass