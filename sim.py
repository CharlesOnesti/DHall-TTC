import sys
import cProfile
import random
import copy
import params
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
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
      self.agent_params = params.Weekday_Dinner # Swap out with other presets from params.py
      self.top_preferences = dict()
      self.final = []
      self.all_cycles = []

      #Number of students
      #Distribution 
      #types of students for each house

  def run_sim(self):
    
    #TODO create the agents from the options and assign prob distributions based on whether is dinner/lunch/weekday/weekend
    def initialize_agents():
      agent_objects = []
      dummy_agents = []
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
              #dummy_agents.extend(newAgents)
              agent_objects.extend(newAgents)
      return agent_objects, dummy_agents
    
 
      
    agent_list, dummys = initialize_agents()
    priority_agent_list = copy.deepcopy(agent_list)
    random.shuffle(priority_agent_list)
    for i in range(len(priority_agent_list)):
      priority_agent_list[i].priority = i
    priority_agent_list.extend(dummys)

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
          if agent.preferences[0] == a_j.initial_house:
            return a_j
        agent.preferences.pop(0)

      return None

    #Run TTC
    self.roundIndex = 0

    while len(priority_agent_list) > 0:
      print("-" * 50, "ROUND ", self.roundIndex)
      self.roundIndex += 1
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
        if len(cycle) == 1:
          if cycle[0].target is None or cycle[0].target.initial_house == cycle[0].initial_house:
            self.final.append(cycle[0])
            priority_agent_list.remove(cycle[0])
      

      # Filter out lists in graph.sccs that are of length one (not a cycle)
      valid_cycles = list(filter(lambda c: len(c) > 1, graph.sccs))

      # Using graph.sccs, goes through and removes agents in cycles from priority_agent_list as well as creates dictionary of matchings
      self.all_cycles.extend(valid_cycles)
      
      if valid_cycles == []:
        #break
        pass
      else:
        for cycle in valid_cycles:
          for i in range(len(cycle)):
            agent = cycle[i]
            self.final.append(agent)
            priority_agent_list.remove(agent)
            agent.assigned_house = agent.target.initial_house
      
    #print("Total Rounds: ", self.roundIndex)

  def printStats(self):
    numberOfSwaps = 0
    sumImprovement = 0
    nonDummyAgents = 0
    preferenceCounter = [0 for i in range(12)]
    houses = ['dunster', 'leverett', 'mather', 'adams', 'lowell', 'quincy', 'winthrop', 'kirkland', 'eliot', 'cabot', 'currier', 'pfoho']
    diningHallNumbers = {x: 0 for x in houses}
    diningHallTradedNumbers = {x: 0 for x in houses}
    priority_preference = []
    for agent in self.final:
      if agent.initial_house != agent.assigned_house:
        numberOfSwaps += 1
      if agent.initial_house not in agent.immutable_preferences:
        houseOrdering = (copy.deepcopy(agent.immutable_preferences))
        houseOrdering.append(agent.initial_house)
      else:
        houseOrdering = copy.deepcopy(agent.immutable_preferences) 
      if agent.type != "Dummy":
        priority_preference.append((agent.priority, houseOrdering.index(agent.assigned_house)))
        if agent.assigned_house != agent.initial_house:
          diningHallTradedNumbers[agent.assigned_house] += 1
        diningHallNumbers[agent.assigned_house] += 1
        preferenceCounter[houseOrdering.index(agent.assigned_house)] += 1
        improvement = (houseOrdering.index(agent.initial_house) - houseOrdering.index(agent.assigned_house))/ max(len(houseOrdering) - 1, 1)
        sumImprovement += improvement
        nonDummyAgents += 1
    return {
      'total_rounds_list': self.roundIndex,
      'total_agents_list': len(self.final),
      'nonDummyAgents_list': nonDummyAgents,
      'averageImprovement_list': float(sumImprovement) / nonDummyAgents,
      'preferenceCounter_list': preferenceCounter,
      'diningHallNumbers_list': diningHallNumbers,
      'diningHallTradedNumbers_list': diningHallTradedNumbers,
      'numberOfSwaps_list': numberOfSwaps,
      'averageCycleLength_list': len(sum(self.all_cycles, [])) / len(self.all_cycles),
      'aggregate_priority-preference:': priority_preference
    }
    

def main():
  iterations = 10 # number of iterations to run

  overall_stats = {
    'total_rounds_list': [],
    'total_agents_list': [],
    'nonDummyAgents_list': [],
    'averageImprovement_list': [],
    'preferenceCounter_list': [],
    'diningHallNumbers_list': [],
    'diningHallTradedNumbers_list': [],
    'numberOfSwaps_list': [],
    'averageCycleLength_list': [],
    'aggregate_priority-preference:': []
  }
  for i in range(iterations):
    def dict_mean(dict_list):
      mean_dict = {}
      for key in dict_list[0].keys():
          mean_dict[key] = sum(d[key] for d in dict_list) / len(dict_list)
      return mean_dict
    sim = Sim()
    sim.run_sim()
    stats = sim.printStats()
    for stat in stats:
      overall_stats[stat].append(stats[stat])

  print("Total Rounds: ", sum(overall_stats['total_rounds_list']) / iterations)
  print("Total Agents: ", sum(overall_stats['total_agents_list']) / iterations)
  print("Number of Non Dummy agents: " , sum(overall_stats['nonDummyAgents_list']) / iterations)
  print("Average Improvement: ", sum(overall_stats['averageImprovement_list']) / iterations)
  print("Preference Counter: ", np.average(overall_stats['preferenceCounter_list'], axis=0))
  print("Dining Hall Numbers: ", dict_mean(overall_stats['diningHallNumbers_list']))
  print("Dining Hall Traded Numbers: ", dict_mean(overall_stats['diningHallTradedNumbers_list']))
  print("Number of Swaps: ", sum(overall_stats['numberOfSwaps_list']) / iterations)
  print("Average Cycle Length", sum(overall_stats['averageCycleLength_list']) / iterations)
  x = np.array(list(map(lambda x: x[0] + 1, sum(overall_stats['aggregate_priority-preference:'], []))))
  y = np.array(list(map(lambda x: x[1], sum(overall_stats['aggregate_priority-preference:'], []))))
  plt.scatter(x, y)
  plt.title('Effect of Priority on Assigned Dining Hall Preference')
  plt.xlabel('Priority Rank')
  plt.ylabel('Achieved Preference')
  m, b = np.polyfit(x, y, 1)
  plt.plot(x, m*x + b, color='red')
  plt.show()


if __name__ == "__main__":
  cProfile.run('main()',"profile.txt")