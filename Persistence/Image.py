import numpy as np
import SubImage as subi
from scipy import misc
import warnings
warnings.filterwarnings("ignore")

class Image():

    # Class constructor
    def __init__(self, image, rows, cols):
        self.__image = image
        self.__rows = rows
        self.__cols = cols
        self.__rows_pixels = len(self.__image)
        self.__cols_pixels = len(self.__image[0])
        self.__rows_quotient = float(len(self.__image) / self.__rows)
        self.__cols_quotient = float(len(self.__image[0]) / self.__cols)
        self.__sub_images = np.empty((self.__rows, self.__cols), dtype=object)
        self.__tile_position = (0, 0)
        self.__resize()

    # Method to resize the image if needed
    def __resize(self):
        print ('\nChecking if resizing is needed...')
        remainder = self.__rows_pixels % self.__rows
        resize = False

        if remainder != 0:
            self.__rows_pixels -= remainder
            resize = True

        remainder = self.__cols_pixels % self.__cols

        if remainder != 0:
            self.__cols_pixels -= remainder
            resize = True

        if resize:
            self.__image = misc.imresize(self.__image, (self.__rows_pixels, self.__cols_pixels))
            print ('Image has been resized, new size: ' + str(self.__cols_pixels) + 'x' + str(self.__rows_pixels))
        else:
            print ('Resizing wasn\'t needed.')

    # Method to set the black tile
    def set_black_tile(self):
        print ('Setting black tile...')
        i = 0
        j = 0
        while i < self.__rows_quotient:
            self.__image[i][j] = [0, 0, 0]
            if j == self.__cols_quotient - 1:
                j = 0
                i += 1
            else:
                j += 1
        print ('Done!')

    # Method to create the subimages storing them in a 2D array with a position value
    def create_sub_images(self):
        print ('Creating sub-images...')
        i = 0
        j = 0
        k = 0
        l = 0
        position = 0

        while i < self.__rows_pixels:
            sub_image = subi.SubImage(self.__image[i:i + self.__rows_quotient, j:j + self.__cols_quotient], position)
            self.__sub_images[k][l] = sub_image
            if j == self.__cols_pixels - self.__cols_quotient:
                j = 0
                i += self.__rows_quotient
            else:
                j += self.__cols_quotient

            if l == len(self.__sub_images[0]) - 1:
                l = 0
                k += 1
            else:
                l += 1

            position += 1
        print ('Done!')

    # Method to get the possible movements
    def possible_movements(self):
        print ('Calculating possible movements...')
        movements = ['Left','Right','Down','Up']
        string = ''
        found = False
        i = 0
        j = 0

        while not found and i < len(self.__sub_images):

            if self.__sub_images[i][j].get_position() == 0:
                found = True
                self.__tile_position = (i,j)

            if not found:

                if j == len(self.__sub_images[0]) - 1:
                    j = 0
                    i += 1
                else:
                    j += 1

        if j - 1 < 0:
            movements.remove('Left')
        if j + 1 > len(self.__sub_images[0]) - 1:
            movements.remove('Right')
        if i + 1 > len(self.__sub_images) - 1:
            movements.remove('Down')
        if i - 1 < 0:
            movements.remove('Up')

        for i in range(0, len(movements), 1):
            string += movements[i] + '. '

        print ('Available Movements: ')
        print (string)

    def swap_images(self, direction):
        if direction == 'Left':
            aux = self.__sub_images[self.__tile_position[0]][self.__tile_position[1]]
            self.__sub_images[self.__tile_position[0]][self.__tile_position[1]] = \
                self.__sub_images[self.__tile_position[0]][self.__tile_position[1] - 1]
            self.__sub_images[self.__tile_position[0]][self.__tile_position[1] - 1] = aux
            print ('Black tile moved successfully!')

        elif direction == 'Right':

            aux = self.__sub_images[self.__tile_position[0]][self.__tile_position[1]]
            self.__sub_images[self.__tile_position[0]][self.__tile_position[1]] = \
                self.__sub_images[self.__tile_position[0]][self.__tile_position[1] + 1]
            self.__sub_images[self.__tile_position[0]][self.__tile_position[1] + 1] = aux
            print ('Black tile moved successfully!')

        elif direction == 'Down':

            aux = self.__sub_images[self.__tile_position[0]][self.__tile_position[1]]
            self.__sub_images[self.__tile_position[0]][self.__tile_position[1]] = \
                self.__sub_images[self.__tile_position[0] + 1][self.__tile_position[1]]
            self.__sub_images[self.__tile_position[0] + 1][self.__tile_position[1]] = aux
            print ('Black tile moved successfully!')

        elif direction == 'Up':

            aux = self.__sub_images[self.__tile_position[0]][self.__tile_position[1]]
            self.__sub_images[self.__tile_position[0]][self.__tile_position[1]] = \
                self.__sub_images[self.__tile_position[0] - 1][self.__tile_position[1]]
            self.__sub_images[self.__tile_position[0] - 1][self.__tile_position[1]] = aux
            print ('Black tile moved successfully!')

        else:
            print ('Please choose a valid position.')

    def save_image(self, is_original):

        if is_original:
            misc.imsave(raw_input('Introduce the directory and image name (with type i.e .png): '), self.__image)
        else:
            i = 0
            j = 0
            k = 0
            l = 0
            image_modified = np.empty((self.__rows_pixels, self.__cols_pixels, 3))

            while i < self.__rows_pixels:
                image_modified[i:i + self.__rows_quotient, j:j + self.__cols_quotient] = \
                    self.__sub_images[k][l].get_image()
                if j == self.__cols_pixels - self.__cols_quotient:
                    j = 0
                    i += self.__rows_quotient
                else:
                    j += self.__cols_quotient

                if l == len(self.__sub_images[0]) - 1:
                    l = 0
                    k += 1
                else:
                    l += 1

            misc.imsave(raw_input('Introduce the directory and image name (with type i.e .png): '),image_modified)

        print ('Image saved successfully!')

    def compare_sub_images(self, to_compare_image):
        print ('Checking if puzzle can be solved...')
        same = True
        i = 0
        j = 0
        k = 0
        l = 0

        if self.__rows_pixels != to_compare_image.__rows_pixels or self.__cols_pixels != to_compare_image.__cols_pixels:
            print("Images cannot be compared because they are no the same size, try again.")
            same = False
        else:
            while i < len(self.__sub_images) and k < len(to_compare_image.get_sub_images()) and l < len(to_compare_image.get_sub_images()[0]):

                if not np.array_equal(self.__sub_images[i][j].get_image(), to_compare_image.get_sub_images()[k][l].get_image()):
                    same = False
                else:
                    same = True
                    k = 0
                    l = 0
                    if j == len(self.__sub_images[0]) - 1:
                        j = 0
                        i += 1
                    else:
                        j += 1

                if not same:
                    if l == len(to_compare_image.get_sub_images()[0]) - 1:
                        l = 0
                        k += 1
                    else:
                        l += 1

        if not same:
            print ('Images aren\'t the same, try again')

        return same

    def assign_index(self, to_compare_image):
        print ('Assigning indexes...')
        i = 0
        j = 0
        k = 0
        l = 0

        while i < len(self.__sub_images):

            if np.array_equal(self.__sub_images[i][j].get_image(), to_compare_image.get_sub_images()[k][l].get_image()):
                to_compare_image.get_sub_images()[k][l].set_position(self.__sub_images[i][j].get_position())

            if l == len(to_compare_image.get_sub_images()[0]) - 1:
                l = 0
                k += 1
            else:
                l += 1

            if l == len(to_compare_image.get_sub_images()[0]) - 1 and k == len(to_compare_image.get_sub_images()) - 1:
                k = 0
                l = 0
                if j == len(self.__sub_images[0]) - 1:
                    j = 0
                    i += 1
                else:
                    j += 1

        print ('Done!')

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_sub_images(self):
        return self.__sub_images

    def get_image(self):
        return self.__image