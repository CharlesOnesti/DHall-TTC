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
from graph import Graph

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
    priority_agent_list = copy.deepcopy(agent_list)
    random.shuffle(priority_agent_list)
    matchings = dict()

    #Randomize Agent_list order
    def find_target(agent, priority_agent_list):
      """Returns id of top priority agent that a certain agent or None 
      Args:
          agent (Agent): agent object
          priority_agent_list ([Agent]): list of agents in random priority order
      Returns:
          id of target agent
      """
      while len(agent.preferences) > 0:
        for a_j in priority_agent_list:
          if agent.preferences[0] == a_j.initial_house:
            return a_j
        agent.preferences.pop()
      return None

    # step 1 find the targets of all agents. so that agents are nodes and their targets are ptrs
    for agent in agent_list:
      agent.target = find_target(agent, priority_agent_list)
        
    # step 2 find cycles in the network
    graph = Graph(priority_agent_list)
    for agent in priority_agent_list:
      if agent.target is not None:
        graph.addEdge(agent, agent.target)
    graph.printSCCs()
    #TODO cycles_list: list of lists ? ex: [[Agent1, Agent2, Agent3], [Agent4, Agent 5], [Agent 7]]

    #remove agents with self loops
    for cycle in cycles_list:
      if len(cycle) == 1:
        if not cycle[0].target:
          priority_agent_list.remove(cycle[0])
    
    
    #Filter out lists in cycles_list that are of length one (not a cycle)
    cycles_list = list(filter(lambda c: len(c) > 1, cycles_list))

    #Using cycles_list, goes through and removes agents in cycles from priority_agent_list as well as creates dictionary of matchings
    for cycle in cycles_list:
      for i in range(len(cycle)):
        agent = cycle[i]
        priority_agent_list.remove(agent)
        if i == (len(cycle) - 1):
          agent.assigned_house = cycle[0]
        else:
          agent.assigned_house = cycle[i + 1]



    # for agent in priority_agent_list:
    #   current = agent.id
    #   visited = []
    #   while current not in visited:
    #     if current not in map(lambda x: x.id, priority_agent_list):
    #       break
    #     visited.append(current)
    #     current = current.target
    #   root = visited.index(current)
    #   for trader in visited[root:]:
    #     trader.assigned_house = agent.preferences[0]
    #     priority_agent_list.remove(trader)
    # step 3 remove agents that have target == None
    


def main():
  sim = Sim()
  sim.run_sim()

if __name__ == "__main__":
  cProfile.run('main()',"profile.txt")


    
