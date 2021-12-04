import sys
import cProfile
import random
import copy
from params import agent_params
from quadagent import QuadAgent
from allriveragent import AllRiverAgent
from rivercentralagent import RiverCentralAgent
from rivereastagent import RiverEastAgent
from riverwestagent import RiverWestAgent
from particularagent import ParticularAgent
from dummyagent import DummyAgent

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
          if agent_type == "QuadAgent":
            newAgents = [QuadAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
            idCounter += self.agent_params[house][agent_type]
            agent_objects.extend(newAgents)
          elif agent_type == "RiverEastAgent":
            newAgents = [RiverEastAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
            idCounter += self.agent_params[house][agent_type]
            agent_objects.extend(newAgents)
          elif agent_type ==  "RiverWestAgent":
            newAgents = [RiverWestAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
            idCounter += self.agent_params[house][agent_type]
            agent_objects.extend(newAgents)
          elif agent_type ==  "RiverCentralAgent":
            newAgents = [RiverCentralAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
            idCounter += self.agent_params[house][agent_type]
            agent_objects.extend(newAgents)
          elif agent_type ==  "AllRiverAgent":
            newAgents = [AllRiverAgent(i, house) for i in range(idCounter, idCounter + self.agent_params[house][agent_type])]
            idCounter += self.agent_params[house][agent_type]
            agent_objects.extend(newAgents)
          elif agent_type ==  "ParticularAgent":
            for targetHouse in self.agent_params[house][agent_type]:
              newAgents = [ParticularAgent(i, house, targetHouse) for i in range(idCounter, idCounter + self.agent_params[house][agent_type][targetHouse])]
              idCounter += self.agent_params[house][agent_type][targetHouse]
              agent_objects.extend(newAgents)
          elif agent_type ==  "DummyAgent":
            for targetHouse in self.agent_params[house][agent_type]:
              newAgents = [DummyAgent(i, house, targetHouse) for i in range(idCounter, idCounter + self.agent_params[house][agent_type][targetHouse])]
              idCounter += self.agent_params[house][agent_type][targetHouse]
              agent_objects.extend(newAgents)
      return agent_objects
    
    #TODO create ttc graph
    def allocate():
      pass
    
    #TODO update dictionary where dictionary is agent id -> top house name mapping; only have agents in dictionary that still need to be matched
    def update_targets(agent_list):
      # for agent in agent_list:
      #   if agent.preferences == []: remove from the TTC procedure
      pass
      
    agent_list = initialize_agents()
    priority_agent_list = random.shuffle(copy.deepcopy(agent_list))
    #Randomize Agent_list order
    def find_target(agent, priority_agent_list):
      while len(agent.preferences) > 0:
        for a_j in priority_agent_list:
          if agent.preferences[0] == a_j.currentHouse:
            return a_j
        agent.preferences.pop()
      return None
    
    for a_i in agent_list:
      a_i.target = find_target(a_i, agent_priority_list)
        
        
          priority_agent_list.remove(a_j)


def main():
  sim = Sim()
  sim.run_sim()

if __name__ == "__main__":
  cProfile.run('main()',"profile.txt")


    
