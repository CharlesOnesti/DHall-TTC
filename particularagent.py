
class ParticularAgent():
  def __init__(self, id, initial_house, target_house):
    """Agent that only wants one house 

    Args:
          id (int): unique integer for agent
          initial_house (String): Lowercase House string which house the person belongs to
          target_house (String): Lowercase House string which house wants to eat in 
    """
    self.id = id
    self.initial_house = initial_house
    self.preferences = [target_house]
     
  def report_pref(self):
    #TODO preferences probability distribution 
    return #Some sort of strategy??


