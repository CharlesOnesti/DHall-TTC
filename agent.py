class Agent():
  def __init__(self, id, initial_house):
    """Agent (either dummy or not) possess preferences and have initial house assignment which does not change

    Args:
        id (int): unique integer for agent
        dummy (bool): True if dummy False if person
        initial_house (String): Lowercase House string which house the person belongs to
    """
    self.id = id
    self.initial_house = initial_house
    self.preferences = []
    self.immutable_preferences = []

  def report_pref(self):
    #TODO preferences probability distribution 
    return #Some sort of strategy??



