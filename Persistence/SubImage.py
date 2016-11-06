class SubImage():

    def __init__(self, image, position):
        self.__image = image
        self.__position = position

    def get_image(self):
        return self.__image

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position