class Node():

    def __init__(self, id, state, depth, action, parent, cost, value):
        self.__id = id
        self.__state = state
        self.__depth = depth
        self.__action = action
        self.__parent = parent
        self.__cost = cost
        self.__value = value

    def get_value(self):
        return self.__value

    def get_state(self):
        return self.__state

    def get_depth(self):
        return self.__depth

    def get_cost(self):
        return self.__cost

    def get_action(self):
        return self.__action

    def get_parent(self):
        return self.__parent

    def get_id(self):
        return self.__id