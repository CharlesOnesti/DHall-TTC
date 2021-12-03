class DummyAgent():
  def __init__(self, id, initial_house, target_house):
    self.id = id
    self.initial_house = initial_house
    self.preferences = [target_house]

  def report_pref(self):
    #TODO preferences probability distribution 
    return #Some sort of strategy??



