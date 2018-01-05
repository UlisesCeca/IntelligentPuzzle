import numpy as np
import Persistence.SubImage as subi
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
        self.__tile_position = (0, 0)
        self.__resize()
        self.__sub_images = {}
        self.__image_representation = np.empty((rows, cols))

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

        for i in range(0, int(self.__rows_quotient), 1):
            for j in range(0, int(self.__cols_quotient), 1):
                self.__image[i][j] = [0, 0, 0]

        print ('Done!')

    # Method to create the subimages storing them in a 2D array with a position value
    def slice_image(self):
        print ('Creating sub-images...')
        sub_images_list = []
        position = 0

        for i in range(0, int(self.__rows_pixels), int(self.__rows_quotient)):
            for j in range(0, int(self.__cols_pixels), int(self.__cols_quotient)):
                sub_images_list.append(subi.SubImage(self.__image[i:i + self.__rows_quotient, j:j + self.__cols_quotient], position))
                position += 1

        print ('Done!')
        return sub_images_list

    def create_indexed_sub_images(self, to_compare_image):
        print ('Assigning indexes...')
        sub_images_list = self.slice_image()
        to_compare_sub_images_list = to_compare_image.slice_image()
        i = 0
        j = 0

        for sub_image in sub_images_list:
            sub_image.set_position(-1)

        for sub_image in sub_images_list:
            for to_compare_sub_image in to_compare_sub_images_list:
                if sub_image.get_position() == -1 and np.array_equal(sub_image.get_image(), to_compare_sub_image.get_image()):
                    self.__sub_images[to_compare_sub_image.get_position()] = sub_image.get_image()
                    self.__image_representation[i][j] = to_compare_sub_image.get_position()

                    if j == len(self.__image_representation[0]) - 1:
                        j = 0
                        i += 1
                    else:
                        j += 1
                    break

        print ('Done!')

    # Method to compare if the ordered and disoredered images are the same
    def compare_sub_images(self, to_compare_image):
        print ('Checking if puzzle can be solved...')
        same = True

        # Check if amount of sub-images are the same
        if len(self.__sub_images) == len(to_compare_image.get_sub_images()):
            # Check if sub-images are the same
            for position, sub_image in self.__sub_images.items():
                if not same:
                    break
                for position2, to_compare_sub_image in to_compare_image.get_sub_images().items():
                    if np.array_equal(sub_image, to_compare_sub_image):
                        same = True
                        break

                    else:
                        same = False
        else:
            same = False

        return same

    # Method to save the image in the computer
    def save_image(self, state, strategy):
        saved_image = np.empty((self.__rows_pixels, self.__cols_pixels, 3))
        k = 0
        l = 0

        for i in range(0, len(state.get_image_representation()), 1):
            for j in range(0, len(state.get_image_representation[0]), 1):
                saved_image[k:k + self.__rows_quotient, l:l + self.__cols_quotient] = \
                    self.__sub_images[self.__image_representation[i][j]]

                if l == self.__cols_pixels - self.__cols_quotient:
                    l = 0
                    k += self.__rows_quotient
                else:
                    l += self.__cols_quotient

            misc.imsave('/output_' + strategy + '/' + i, saved_image)


    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_sub_images(self):
        return self.__sub_images

    def get_image_representation(self):
        return self.__image_representation
