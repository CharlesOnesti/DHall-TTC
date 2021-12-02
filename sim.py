import sys
import cProfile

from agent import Agent

class Sim():
  def __init__(self, weekday, lunch, agents_to_initialize):
      """[summary]

      Args:
          weekday (bool): True if want to simulate a weekday (False if weekend) 
          lunch (bool): True if want to simulate a lunch (False if dinner) 
      """
      self.weekday = weekday
      self.lunch = lunch
      self.agents_to_initialize = agents_to_initialize
      self.top_preferences = dict()

  def run_sim(self):
    
    #TODO create the agents from the options and assign prob distributions based on whether is dinner/lunch/weekday/weekend
    def initialize_agents():
        # agents = list(map(lambda x: Agent(x[0], False, x[1]), enumerate(self.agents_to_initialize)))
        # return agents
      pass
    
    #TODO create ttc graph
    def allocate():
      pass
    
    #TODO update dictionary where dictionary is agent id -> top house name mapping; only have agents in dictionary that still need to be matched
    #ex: {1: 'adams', 2: 'quincy', 3: 'dunster}
    def update_target():
        pass

#Adapted from sim.py in CS136 Programming Assignment 2
def parse_agents(args):
  """
  Each element is a class name like "SomethingAgent", with an optional
  count appended after a comma.  I.e. "Dummy,dunster,adams,5"
  or "ParticularAgent,dunster,adams,5" or "QuadAgent,dunster,5"
  Returns an array with a list of class names, each repeated the
  specified number of times.
  """
  ans = []
  for c in args:
    s = c.split(',')
    if len(s) == 3:
      name, house, count = s
      ans.extend([(name, house)]*int(count))
    elif len(s) == 4:
      name, house, pref, count = s
      ans.extend([(name, house, pref)]*int(count))
    else:
      raise ValueError("Bad argument: %s\n" % c)
  return ans

def main(args):
  [_, weekday, lunch] = args
  sim = Sim(weekday, lunch, parse_agents(args[3:]))
  sim.run_sim()

if __name__ == "__main__":
  cProfile.run('main(sys.argv)',"profile.txt")


    
