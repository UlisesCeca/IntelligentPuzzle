import numpy as np

class State():

    def __init__(self, representation, black_tile_position, sub_images):
        self.__sub_images = sub_images
        self.__image_representation = representation
        if black_tile_position == (-1, -1): # Check if we must search for the black tile
            self.__black_tile_position = self.__find_black_tile(black_tile_position)
        else:
            self.__black_tile_position = black_tile_position

    # Method to find the position of the black tile
    def __find_black_tile(self, black_tile_position):
        if black_tile_position == (-1, -1): # If we don't have the position we search it
            for i in range(0, len(self.__image_representation), 1):
                for j in range(0, len(self.__image_representation[0]), 1):
                    if self.__image_representation[i][j] == 0:
                        return (i, j)

    # Method to get the possible movements
    def possible_movements(self):
        movements = ['Left', 'Right', 'Down', 'Up']

        if self.__black_tile_position[1] - 1 < 0:
            movements.remove('Left')

        if self.__black_tile_position[1] + 1 > len(self.__image_representation[0]) - 1:
            movements.remove('Right')

        if self.__black_tile_position[0] + 1 > len(self.__image_representation) - 1:
            movements.remove('Down')

        if self.__black_tile_position[0] - 1 < 0:
            movements.remove('Up')

        return movements

    # Method to swap the position of 2 tiles
    def swap_images(self, direction):
        new_representation = np.copy(self.__image_representation)
        new_black_tile_position = self.__black_tile_position

        if direction == 'Left':
            # Movement in representation
            aux = new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]]
            new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]] = \
                new_representation[self.__black_tile_position[0]][self.__black_tile_position[1] - 1]
            new_representation[self.__black_tile_position[0]][self.__black_tile_position[1] - 1] = aux

            # Tile update
            new_black_tile_position = (new_black_tile_position[0], new_black_tile_position[1] - 1)

        elif direction == 'Right':
            # Movement in representation
            aux = new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]]
            new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]] = \
                new_representation[self.__black_tile_position[0]][self.__black_tile_position[1] + 1]
            new_representation[self.__black_tile_position[0]][self.__black_tile_position[1] + 1] = aux

            # Tile update
            new_black_tile_position = (new_black_tile_position[0], new_black_tile_position[1] + 1)

        elif direction == 'Down':
            # Movement in representation
            aux = new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]]
            new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]] = \
                new_representation[self.__black_tile_position[0] + 1][self.__black_tile_position[1]]
            new_representation[self.__black_tile_position[0] + 1][self.__black_tile_position[1]] = aux

            # Tile update
            new_black_tile_position = (new_black_tile_position[0] + 1, new_black_tile_position[1])

        elif direction == 'Up':
            # Movement in representation
            aux = new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]]
            new_representation[self.__black_tile_position[0]][self.__black_tile_position[1]] = \
                new_representation[self.__black_tile_position[0] - 1][self.__black_tile_position[1]]
            new_representation[self.__black_tile_position[0] - 1][self.__black_tile_position[1]] = aux

            # Tile update
            new_black_tile_position = (new_black_tile_position[0] - 1, new_black_tile_position[1])

        return new_representation, new_black_tile_position, self.__sub_images

    def get_image_representation(self):
        return self.__image_representation
