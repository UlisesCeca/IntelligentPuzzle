import Persistence.Image as img
from scipy import misc

def main():
    ordered = object
    disordered = object
    ordered_created = False
    disordered_created = False
    exit_program = False

    while not exit_program:
        choice = int(input("""\nPlease choose an option:
        1. Load ordered image.
        2. Load disordered image.
        3. Show possible movements list.
        4. Make a movement.
        5. Save image.
        6. Exit.\n"""))

        if choice == 1:
            image = misc.imread(raw_input('Introduce the image full address: '))
            cols = int(input('Insert cols amount: '))
            rows = int(input('Insert rows amount: '))
            ordered = img.Image(image, rows, cols)
            ordered.create_sub_images()
            ordered.set_black_tile()
            ordered.assign_index(ordered)
            print ('Image loaded successfully!')
            ordered_created = True

        elif choice == 2:
            if not ordered_created:
                print('\nYou must load the ordered image first\n')
            else:
                image = misc.imread(raw_input('Introduce the image full address: '))
                disordered = img.Image(image, ordered.get_rows(), ordered.get_cols())
                disordered.create_sub_images()
                if disordered.compare_sub_images(ordered):
                    print ('Image loaded successfully, it matches!')
                    ordered.assign_index(disordered)
                    disordered_created = True

        elif choice == 3:
            if not disordered_created:
                print('\nYou must load the disordered image first\n')
            else:
                disordered.possible_movements()

        elif choice == 4:
            if not disordered_created:
                print('\nYou must load the disordered image first\n')
            else:
                disordered.possible_movements()
                movement = raw_input()
                disordered.swap_images(movement)

        elif choice == 5:
            choice_save = int(input("""\n Choose which image you'd like to save:
            1. Original Ordered.
            2. Original Disordered.
            3. Modified.\n"""))

            if choice_save == 1:
                if not ordered_created:
                    print('\nYou must load the ordered image first\n')
                else:
                    ordered.save_image(True)

            elif choice_save == 2:
                if not disordered_created:
                    print('\nYou must load the disordered image first\n')
                else:
                    disordered.save_image(True)

            elif choice_save == 3:
                if not disordered_created:
                    print('\nYou must load the disordered image first\n')
                else:
                    disordered.save_image(False)

        elif choice == 6:
            exit_program = True

if __name__ == "__main__":
    main()
