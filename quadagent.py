import params
import random
import copy

class QuadAgent():
  def __init__(self, id, initial_house):
    self.id = id
    self.initial_house = initial_house
    temp_pref = copy.deepcopy(params.quadHouses)
    random.shuffle(temp_pref)
    self.preferences = temp_pref
    self.immutable_preferences = copy.deepcopy(temp_pref)
    self.priority = None
    self.target = None
    self.assigned_house = initial_house
    self.type = "Quad"




