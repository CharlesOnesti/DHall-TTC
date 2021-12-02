import sys
import cProfile
from params import agent_params
from agent import Agent

class Sim():
  def __init__(self):
      self.weekday = True
      self.lunch = False
      self.top_preferences = dict()
      self.agent_params = agent_params

      #Number of students
      #Distribution 
      #types of students for each house

  def run_sim(self):
    
    #TODO create the agents from the options and assign prob distributions based on whether is dinner/lunch/weekday/weekend
    def initialize_agents():
      agent_objects = []
      idCounter = 0
      for house in self.agent_params:
        for agent_type in self.agent_params[house]:
          match agent_type:
            case "QuadAgent":
              newAgents = [QuadAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
              idCounter += self.agent_params[house][agent_type]
              agent_objects.extend(newAgents)
            case "RiverEastAgent":
              newAgents = [RiverEastAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
              idCounter += self.agent_params[house][agent_type]
              agent_objects.extend(newAgents)
            case "RiverWestAgent":
              newAgents = [RiverWestAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
              idCounter += self.agent_params[house][agent_type]
              agent_objects.extend(newAgents)
            case "RiverCentralAgent":
              newAgents = [RiverCentralAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
              idCounter += self.agent_params[house][agent_type]
              agent_objects.extend(newAgents)
            case "AllRiverAgent":
              newAgents = [AllRiverAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
              idCounter += self.agent_params[house][agent_type]
              agent_objects.extend(newAgents)
            case "ParticularAgent":
              for targetHouse in self.agent_parms[house][agent_type]:
                newAgents = [ParticularAgent(i, house, targetHouse) for i in range(idCounter, idCounter + self.agent_params[house][agent_type][targeHouse])]
                idCounter += self.agent_params[house][agent_type][targeHouse]
                agent_objects.extend(newAgents)
            case "DummyAgent":
              for targeHouse in self.agent_params[house][agent_type]:
                newAgents = [DummyAgent(i, house, targetHouse) for i in range(idCounter, idCounter + self.agent_params[house][agent_type][targeHouse])]
                idCounter += self.agent_params[house][agent_type][targeHouse]
                agent_objects.extend(newAgents)

      return agent_objects
    
    #TODO create ttc graph
    def allocate():
      pass
    
    #TODO update dictionary where dictionary is agent id -> top house name mapping; only have agents in dictionary that still need to be matched
    #ex: {1: 'adams', 2: 'quincy', 3: 'dunster}
    def update_target():
        pass

def main():
  sim = Sim()
  sim.run_sim()

if __name__ == "__main__":
  cProfile.run('main()',"profile.txt")


    
