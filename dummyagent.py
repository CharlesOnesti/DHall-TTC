class DummyAgent():
  def __init__(self, id, initial_house, target_house):
    self.id = id
    self.initial_house = initial_house
    self.preferences = [target_house]
    self.immutable_preferences = [target_house]
    self.target = None
    self.priority = None
    self.assigned_house = initial_house
    self.type = "Dummy"




