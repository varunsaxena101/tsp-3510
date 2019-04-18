## Varun Saxena and Ahan Shah
# Simulated Annealing

import sys
from scipy.spatial import distance
import random
import math
import time

def generateGreedy():
    tour_length = 0
    tour_sequence = [1]

    visited_cities = set()
    curr_node = 1
    visited_cities.add(1)

    while len(visited_cities) != len(cities):
        #print("visited cities", visited_cities)
        #print("current node", curr_node)

        shortest_dist = sys.maxsize
        shortest_node = None
        for i in range(1, len(cities) + 1):
            if i in visited_cities:
                continue
            
            dist = distance.euclidean(cities[curr_node], cities[i])
            if dist < shortest_dist:
                #print("found closest node", i, "with length", dist)
                shortest_dist = dist
                shortest_node = i

        curr_node = shortest_node
        visited_cities.add(shortest_node)

        tour_length += shortest_dist
        tour_sequence.append(shortest_node)

    # return to node 1
    dist = distance.euclidean(cities[curr_node], cities[1])
    tour_length += dist
    tour_sequence.append(1)

    #print("END GENERATE GREEDY")
    return tour_length, tour_sequence

def getNeighborPath(path, c1, c2):
    if c1 == c2:
        return path
    
    # make sure c1 is less than c2
    if c1 > c2:
        temp = c1
        c1 = c2
        c2 = temp

    path1 = path[:c1]
    path2 = path[c1:c2+1]
    path2.reverse()
    path3 = path[c2+1:]

    return path1 + path2 + path3

def getTourLength(path):
    tour_length = 0

    for i in range(len(path) - 1):
        #print("Tour length of", distance.euclidean(cities[path[i]], cities[path[i+1]]), "between", path[i], "and", path[i+1])
        tour_length += distance.euclidean(cities[path[i]], cities[path[i+1]])

    return tour_length


start_time = time.time()

#print(sys.argv)
args = sys.argv

# process inputs
input_coords_file = args[1]
output_file = args[2]
time_allowed = float(args[3]) - 0.5     #take off 0.5 seconds to account for writing to output

# read in coordinates
input_file = open(input_coords_file, "r")

line = input_file.readline()

cities = {}
while(line is not ''):
    a = line.split(" ")
    cities[int(float(a[0]))] = (int(float(a[1])), int(float(a[2])))
    line = input_file.readline()

# start with greedy route

path_length, path_sequence = generateGreedy()

temperature = start_time - time.time() + time_allowed

while (time.time() - start_time < time_allowed):
    # choose two cities on the tour randomly and reverse order
    index1 = random.randint(1, len(cities)-1)
    index2 = random.randint(1, len(cities)-1)

    neighbor_sequence = getNeighborPath(path_sequence[:], index1, index2)
    neighbor_length = getTourLength(neighbor_sequence)

    # if this tour is better accept it
    if neighbor_length < path_length:
        #print("found better path")
        path_length = neighbor_length
        path_sequence = neighbor_sequence
    else:
        # if its worse, accept it according to some probability
        if math.exp((path_length - neighbor_length)/(temperature*10)) > random.random():
            # override with worse path
            print("using worse path")
            path_length = neighbor_length
            path_sequence = neighbor_sequence

    # repeat and lower temperature each time
    temperature = start_time - time.time() + time_allowed

    print("temperature: ", temperature*10)
    print("path length:", path_length)
    print("time left:", temperature)


# write to output file
for i in range(len(path_sequence)):
    path_sequence[i] = str(path_sequence[i])

f = open(output_file, "w")
string1 = str(path_length)
separator = " "
seq = separator.join(path_sequence)
f.write(string1 + '\n' + seq)
