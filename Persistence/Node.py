import random as rd

class Node():

    def __init__(self, state, depth, action, parent, cost):
        self.__state = state
        self.__depth = depth
        self.__action = action
        self.__parent = parent
        self.__cost = cost
        self.__value = rd.random(0,1000)

    def __str__(self):
        return "Value: " + self.__value + "Depth: " + self.__depth + "State: " + self.__state +\
            "Cost: " + self.__cost
