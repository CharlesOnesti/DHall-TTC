import params
import random
import copy

class RiverCentralAgent():
  def __init__(self, id, initial_house):
    self.id = id
    self.initial_house = initial_house
    temp_pref = copy.deepcopy(params.riverCentralHouses)
    random.shuffle(temp_pref)
    self.preferences = temp_pref

  def report_pref(self):
    #TODO preferences probability distribution 
    return #Some sort of strategy??



