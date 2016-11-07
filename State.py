

class State():

    def __init__(self,__image):
        self.__image=__image
        self.positions = self.get_allPositions()


    def isValid(self,state):
        if self.positions in self.Successor(state):
                return True
        else:
            return False




        # Calling just from ordered image so "positions" would be the goal state.

    def isGoal(self, state):


        if (self.__positions == state):
            return True
        else:
            return False
            # State es la imagen en una iteración a través de pedir lo


    def get_allPositions(self):
        positions=[]
        for i in range (0,(self.__image.__subimages).length,1):
            positions[i]=self.__image.__sub_images[i].__position
        return positions





    def Successor(self, state):
        succesors = []
        actual_movements = state.__image.possible_movements()
        cost = 1

        for i in range(0, actual_movements.length, 1):
            succesors.append(actual_movements[i], state, cost)

        return succesors


