import Persistence.Node as nd
import Persistence.Frontier as fr
import Persistence.State_Space as sp

class Problem():

    def __init__(self, goal_state, initial_state):
        self.__state_space = sp.State_Space(goal_state)
        self.__initial_state = initial_state
        self.__id = 1

    def limited_search(self, strategy, max_depth):
        solution = False
        current_node = None
        frontier = fr.Frontier()
        root_node = nd.Node(0, self.__initial_state, 0, None, None, 0, 0)
        frontier.insert(root_node)
        print('Finding solution...')

        # Seach loop
        while not solution and not frontier.is_empty():
            current_node = frontier.get_node()

            if self.__state_space.is_goal(current_node.get_state()):
                solution = True

            else:
                successors_list = self.__state_space.calculate_successors(current_node.get_state())
                nodes_list = self.search_strategies(successors_list, current_node, strategy, max_depth)
                frontier.insert_list(nodes_list)

        if solution:
            print(current_node.get_state().get_image_representation())
            return current_node

        else:
            return None


    def search_strategies(self, successors_list, parent_node, strategy, max_depth):
        nodes_list = []
        value = 0

        for successor in successors_list:
            depth = parent_node.get_depth() + 1
            cost = parent_node.get_cost() + 1

            if strategy == 'BFS':
                    value = depth

            elif strategy == 'DFS' or strategy == 'DLS' or strategy == 'IDS':
                    value = depth * -1

            elif strategy == 'UCS':
                    value = cost

            if depth <= max_depth:
                nodes_list.append(nd.Node(self.__id, successor[1], depth, successor[0], parent_node, cost, value))
                self.__id += 1

        return nodes_list

    def search(self, strategy, max_depth, incremental_depth):
        current_depth = incremental_depth
        solution = None

        while not solution and current_depth <= max_depth:
            solution = self.limited_search(strategy, max_depth)
            current_depth += 1

        if solution:
            print('Solution found!')

        else:
            print('Solution not found!')

        return solution
