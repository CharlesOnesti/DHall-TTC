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
      self.agent_params = params.Weekday_Lunch
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
    
    random.Random(1).shuffle(priority_agent_list)
    priority_agent_list.extend(dummys)
    # random.Random(1).shuffle(dummys)
    # priority_agent_list.extend(dummys)
    # print("Priority:")
    # for i in (priority_agent_list):
    #   print("ID:", i.id)
    #   print("AGENT: ", i.id, ": ",i.preferences, ' Initial house: ', i.initial_house, " Target: ", i.target)
    #   print('')


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
        #print(cycle)
        if len(cycle) == 1:
          if cycle[0].target is None or cycle[0].target.initial_house == cycle[0].initial_house:
            print("Removing: ", cycle[0].id)
            self.final.append(cycle[0])
            priority_agent_list.remove(cycle[0])
      

      # Filter out lists in graph.sccs that are of length one (not a cycle)
      valid_cycles = list(filter(lambda c: len(c) > 1, graph.sccs))

      # Using graph.sccs, goes through and removes agents in cycles from priority_agent_list as well as creates dictionary of matchings
      print('REMOVED: ', list(map(lambda x: list(map(lambda y: y.id, x)),valid_cycles)))
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
      
      print("REMAINING: ", list(map(lambda x: x.id, priority_agent_list)))
    #print("Total Rounds: ", self.roundIndex)

  def printStats(self):
    numberOfSwaps = 0
    sumImprovement = 0
    nonDummyAgents = 0
    preferenceCounter = [0 for i in range(12)]
    houses = ['dunster', 'leverett', 'mather', 'adams', 'lowell', 'quincy', 'winthrop', 'kirkland', 'eliot', 'cabot', 'currier', 'pfoho']
    diningHallNumbers = {x: 0 for x in houses}
    diningHallTradedNumbers = {x: 0 for x in houses}
    for agent in self.final:
      print('ID: ', agent.id, ' ' * (7-len(str(agent.id))), 'Initial house: ', agent.initial_house, ' ' * (10-len(agent.initial_house)),'Assigned house: ', agent.assigned_house, ' ' * (10-len(agent.assigned_house)), 'Immutable_preferences: ', agent.immutable_preferences)
      if agent.initial_house != agent.assigned_house:
        numberOfSwaps += 1
      
      if agent.initial_house not in agent.immutable_preferences:
        houseOrdering = (copy.deepcopy(agent.immutable_preferences))
        houseOrdering.append(agent.initial_house)
        print(houseOrdering)
      else:
        houseOrdering = copy.deepcopy(agent.immutable_preferences)
      
      print(agent.type)
      
      if agent.type != "Dummy":
        if agent.assigned_house != agent.initial_house:
          diningHallTradedNumbers[agent.assigned_house] += 1
        diningHallNumbers[agent.assigned_house] += 1
        preferenceCounter[houseOrdering.index(agent.assigned_house)] += 1
        improvement = (houseOrdering.index(agent.initial_house) - houseOrdering.index(agent.assigned_house))/ max(len(houseOrdering) - 1, 1)
        sumImprovement += improvement
        nonDummyAgents += 1

    print("Total Rounds: ", self.roundIndex)
    print("Total Agents: ", len(self.final))
    print("Number of Non Dummy agents: " , nonDummyAgents)
    print("Average Improvement: ", float(sumImprovement) / nonDummyAgents)
    print("Preference Counter: ", preferenceCounter)
    print("Dining Hall Numbers: ", diningHallNumbers)
    print("Dining Hall Traded Numbers: ", diningHallTradedNumbers)
    print("Number of Swaps: ", numberOfSwaps)
    


    # numCycles = 0
    # for cycle in self.all_cycles:
    #   numCycles += len(cycle)
    print("Average Cycle Length", len(sum(self.all_cycles, [])) / len(self.all_cycles))
    
    

def main():
  sim = Sim()
  sim.run_sim()
  sim.printStats()
if __name__ == "__main__":
  cProfile.run('main()',"profile.txt")