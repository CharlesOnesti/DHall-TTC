import params
import random
import copy

class RiverEastAgent():
  def __init__(self, id, initial_house):
    self.id = id
    self.initial_house = initial_house
    temp_pref = copy.deepcopy(params.riverEastHouses)
    random.shuffle(temp_pref)
    self.preferences = temp_pref
    self.immutable_preferences = copy.deepcopy(temp_pref)
    self.priority = None
    self.target = None
    self.assigned_house = initial_house
    self.type = "RiverEast"




