import queue

class Frontier:

    def __init__(self):
        self.__list = queue.PriorityQueue()

    # Method to insert nodes into the frontier
    def insert(self, node):
        self.__list._put([node.get_value(), node.get_id(), node])

    # Method to inser a list of nodes
    def insert_list(self, nodes_list):
        for node in nodes_list:
            self.insert(node)

    # Method to get and remove nodes from the frontier
    def get_node(self):
        if self.__list:
            return self.__list._get()[2]

    def is_empty(self):
        if self.__list.empty():
            return True
        else:
            return False
