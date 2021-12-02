import params
import random

class RiverWestAgent():
  def __init__(self, id, initial_house):
    self.id = id
    self.initial_house = initial_house
    self.preferences = random.shuffle(params.riverWestHouses)

  def report_pref(self):
    #TODO preferences probability distribution
    return #Some sort of strategy??



