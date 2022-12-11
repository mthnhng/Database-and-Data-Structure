#Travelling salesman problems
from sys import maxsize

#task 1

#load parcels function
def load_parcels(path, unsorted_parcels):
    bean_arr = []
    bean_bag = []

    for i in range(len(path)):
        for j in range(len(unsorted_parcels)):
            if path[i] == unsorted_parcels[j]:
                #add parcels which deliver to the same city into one bean bag
                bean_bag.append(unsorted_parcels[j])

        #add the bean bag to the bean arrangement and re-empty the bean bag for next destination
        bean_arr.append(bean_bag)
        bean_bag = []

    return bean_arr

#load bean function
def load_beans(bean_arr, door_num):
    vehicle = []
    
    if door_num == 1:
        vehicle.append(bean_arr)
    
    elif door_num == 2:
        door1 = bean_arr[:len(bean_arr)//2]
        door2 = bean_arr[len(bean_arr)//2:]

        vehicle.append(door1)
        vehicle.append(door2)
    
    return vehicle

#unload function
def unload_beans(vehicle):
    for i in range(len(vehicle)):
        for j in range(len(vehicle[i])):
            vehicle[i].pop(0)

    return vehicle
        

#task 2
#create a function that permutates all the elements in the list that will generate all the possible paths stored in an array
def possible_solution(graph):
    if len(graph) == 0:
        return []
    elif len(graph) == 1:
        return [graph]

    #create an empty list that will store all the possible paths
    ran_solution = []
    for i in range(len(graph)):
        route = graph[i]
        #Extract tsp[i] or route from the list, remain_tsp is the remaining list
        remain_tsp = graph[:i] + graph[i+1:]
        #generating all permutaions where route is the first element
        for j in possible_solution(remain_tsp):
            ran_solution.append([route] + j)
    
    return ran_solution

#implementation of travelling salesman problem
def travellingsaleman(graph, init):
    
    #store the remaining cities apart from the initial city
    remain_city = []
    for i in range(len(graph)):
        if i != init:
            remain_city.append(i)
    
    #the maximum number Python can handle
    min_cost = maxsize
    possible_path = possible_solution(remain_city)

    #cost array is used to store the cost of each path, optimum_path array is the path with the lowest cost, path array is the optimum_path in letters
    cost = []
    optimum_path = []
    path = []

    for i in possible_path:
        current_cost = 0

        #calculate current cost
        key = init
        for j in i:
            current_cost += graph[key][j]
            key = j
        current_cost += graph[key][init]

        #update minimum and store all the cost coressponding to each path
        min_cost = min(min_cost, current_cost)
        cost.append(current_cost)
    
    #append the paths with the lowest cost to the array
    for i in range(len(cost)):
        if cost[i] == min_cost:
            optimum_path.append(possible_path[i])
    
    print("Minimum cost: ", min_cost)

    #Change the path from numbers to letter, there are always 2 optimum path, so choose the fiest one
    for i in optimum_path[0]:
        if i == 1:
            path.append("A")
        elif i == 2:
            path.append("B")
        elif i == 3:
            path.append("C")
    
    return path
    
#sample program
def main():
    #sample data, there are 4 cities including inital city, city A, city B and city C.
    graph = [[0, 20, 45, 15], 
             [20, 0, 25, 30],
             [45, 25, 0, 10], 
             [15, 30, 10, 0]]

    door_num = int(2)
    
    #Assume that the init city named city 0
    print(travellingsaleman(graph, 0))

    #Sample data for the parcels, each item in the list is the desination of the following parcel
    unsorted_percels = ["A","C","B","C","B","A","C","B","B","A","C"]

    print(load_parcels(travellingsaleman(graph, 0), unsorted_percels))

    print(load_beans(load_parcels(travellingsaleman(graph, 0), unsorted_percels), door_num))

    print(unload_beans(load_beans(load_parcels(travellingsaleman(graph, 0), unsorted_percels), door_num)))

if __name__ == "__main__":
    main()