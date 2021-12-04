import sys
import cProfile
import random
import copy
import params
from quadagent import QuadAgent
from allriveragent import AllRiverAgent
from rivercentralagent import RiverCentralAgent
from rivereastagent import RiverEastAgent
from riverwestagent import RiverWestAgent
from particularagent import ParticularAgent
from dummyagent import DummyAgent
from graph import Graph

class Sim():
  def __init__(self):
      self.top_preferences = dict()
      self.agent_params = params.test_params_3
      self.final = []

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
    
 
      
    agent_list = initialize_agents()
    priority_agent_list = copy.deepcopy(agent_list)
    
    random.Random(1).shuffle(priority_agent_list)
    print("Priority:")
    for i in (priority_agent_list):
      print(i.id)
      print("AGENT: ", i.id, ": ",i.preferences, ' initial house: ', i.initial_house, "Target: ", i.target)


    #Randomize Agent_list order
    def find_target(agent, p_agent_list):
      """Returns id of top priority agent that a certain agent or None 
      Args:
          agent (Agent): agent object
          priority_agent_list ([Agent]): list of agents in random priority order
      Returns:
          agent
      """
      while len(agent.preferences) > 0:
        for a_j in p_agent_list:
          # print(len(agent.preferences))
          if agent.preferences[0] == a_j.initial_house:
            # print("NEW TARGET: ", a_j)
            return a_j
        agent.preferences.pop(0)

      return None

    #Run TTC
    roundIndex = 0
    while len(priority_agent_list) > 0:
      print("-" * 50, "ROUND ", roundIndex)
      roundIndex += 1
      print("LENGTH: ", len(priority_agent_list))
      # step 1 find the targets of all agents. so that agents are nodes and their targets are ptrs
      for agent in priority_agent_list:
        agent.target = find_target(agent, priority_agent_list)
      
      # step 2 create edges in the network
      graph = Graph(priority_agent_list)
      for agent in priority_agent_list:
        if agent.target is not None:
          graph.addEdge(agent, agent.target)

      # find cycles
      graph.findSCCs()

      # remove agents with self loops
      for cycle in graph.sccs:
        #print(cycle)
        if len(cycle) == 1:
          if cycle[0].target is None or cycle[0].target == cycle[0].initial_house :
            self.final.append(cycle[0])
            priority_agent_list.remove(cycle[0])
      

      # Filter out lists in graph.sccs that are of length one (not a cycle)
      valid_cycles = list(filter(lambda c: len(c) > 1, graph.sccs))

      # Using graph.sccs, goes through and removes agents in cycles from priority_agent_list as well as creates dictionary of matchings
      print(valid_cycles)
      if valid_cycles == []:
        break
        
      for cycle in valid_cycles:
        for i in range(len(cycle)):
          agent = cycle[i]
          self.final.append(agent)
          priority_agent_list.remove(agent)
          if i == (len(cycle) - 1):
            agent.assigned_house = cycle[0].initial_house
          else:
            agent.assigned_house = cycle[i + 1].initial_house

  def printMatchings(self):    
    for agent in self.final:
      print('ID: ', agent.id, ' ' * (10-len(str(agent.id))), 'Initial house: ', agent.initial_house, ' ' * (10-len(agent.initial_house)),'Assigned house: ', agent.assigned_house)

def main():
  sim = Sim()
  sim.run_sim()
  sim.printMatchings()

if __name__ == "__main__":
  cProfile.run('main()',"profile.txt")