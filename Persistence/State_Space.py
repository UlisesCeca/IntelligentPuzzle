import numpy as np
import Persistence.State as st

class State_Space():

    def __init__(self, goal_state):
        self.__goal_state = goal_state

    # Method to know if the given state is valid
    def is_valid(self, state):
        if state in self.calculate_successors(state):
            return True
        else:
            return False

    # Method to get the successors of a given state
    def calculate_successors(self, state):
        successors = []
        cost = 1
        movements = state.possible_movements()

        for movement in movements:
            state_values = state.swap_images(movement)
            new_state = st.State(state_values[0], state_values[1], state_values[2])
            successors.append((movement, new_state, cost))

        return successors

    # Method to know if a given state is the goal
    def is_goal(self, state):
        return np.array_equal(self.__goal_state.get_image_representation(), state.get_image_representation())
