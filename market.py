"""CREATE AN AGENT ENVIRONMENT"""
"""dEFINE AGENT PARAMETERS"""

data = ['a','i'] #list
personalities = ['F','S']
print (data[1])

"""create Agent"""
def make_agent(data, personality):
    return [data, personality]

agent_one =  make_agent(data[1],personalities[0]) #call functions
print("Agent:",agent_one) #print results

"""create identical population"""
def make_population_identical(N):
    population = []
    for i in range(N):
        agent = make_agent(data[i], personalities[0])
        population.append(agent)
    return population

populations_test = make_population_identical(5)  #call function
print("Identical Population:",populations_test)   #print results

"""create Random Population"""
import random
def make_population_random(N):
    population = []
    for i in range(N):
        d = random.choice(data)
        p = random.choice(personalities)
        agent = make_agent(d, p)
        population.append(agent)
    return population

def count(Population):
    t = 0.0 #to make it float!
    for agent in Population:
        if agent[0] == 'a':
            t = t+1
    return t / len(Population)

prop_a = count(make_population_random(20))
print("Random Population:",make_population_random(20))
print('The proportion of [a] in the population is',prop_a) 

"""MAKE AGENTS INTERACT"""
"""SELECT RANDOM AGENTS"""
from numpy.random import choice

def choose_pair(population):
    i = random.randint(0, len(population) - 1)
    j = random.randint(0, len(population) - 1)
    while i == j:
        j = random.randint(0, len(population) - 1) #change if the same agent
    return population[i],population[j]

listener, producer = choose_pair(make_population_random(20))
print('The population is', make_population_random(20))
print('this is the chosen pair', listener, producer)
print('The listener is', listener)
print('The producer is', producer)

"""Make agent Interact"""
from copy import deepcopy
def interact_test(listener, producer):
    if listener[0] == producer[0]:
        return listener
    else:
        if listener[1]=="S": #exit if are agent stubborn
            return listener
        else:
            listener[0] = deepcopy(producer[0])
    return listener #Omit this when running the simulation

updated_listener = interact_test(listener,producer)
print('after interacting,the listener is', updated_listener)


"""SIMULATE REPEATED INTERACTION"""
"""INTERACT WITHOUT RETURNING VALUES"""
def interact(listener,producer):
    if listener[0] == producer[0]:
        pass #do nothing
    else:
         listener[0] = deepcopy(producer[0])

"""Interact n agents k times"""
def simulate(n, k):
    population = make_population_random(n)
    proportion = [] #create list to store proportions after every interaction
    for i in range(k):
        pair = choose_pair(population) #choose a pair from location
        listener, producer = choose_pair(population)
        interact(listener, producer) #make the chosen pair interact
        proportion.append(count(population))
    return population, proportion

population, propotion = simulate(20, 500) #Simulate 500 intercations between 20 agents
print ("Proportion after 500 interactions:",population)


"""visualize populations change after k interactions"""
import matplotlib.pyplot as plt #importing a plotting library
plt.title('changes in the proportion of [a] over time') #and add some detail to plot
plt.ylabel('Proportion [a] users')
plt.xlabel('Time [No. of interaction]')
plt.plot(propotion)
plt.show()


"""increase agents and interactions"""
population, proportion = simulate(200, 5000)
#print "Final population:",population
plt.plot(proportion)
plt.show()
"""simulate iteration 20 times"""
def batch_simulate(n,k,s):
    batch_proportions=[]
    for i in range(s):
        population, proportion = simulate(n, k)
        batch_proportions.append(proportion)

results =batch_simulate(200,5000,20)
for i in results:
    plt.plot(i)
    plt.show()