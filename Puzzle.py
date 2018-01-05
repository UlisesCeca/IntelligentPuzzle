import Persistence.Image as img
from scipy import misc
import Persistence.Problem as pr
import Persistence.State as st
import os
import shutil as sh
import time as tm

def main():
    ordered = object
    disordered = object
    goal_state = object
    initial_state = object
    ordered_created = False
    disordered_created = False
    exit_program = False

    while not exit_program:
        choice = int(input("""\nPlease choose an option:
        1. Load ordered image.
        2. Load disordered image.
        3. Solve problem.
        4. Exit.\n"""))

        if choice == 1:
            image = misc.imread(input('Introduce the image full address: '))
            cols = int(input('Insert cols amount: '))
            rows = int(input('Insert rows amount: '))
            ordered = img.Image(image, rows, cols)
            ordered.set_black_tile()
            ordered.create_indexed_sub_images(ordered)
            goal_state = st.State(ordered.get_image_representation(), (0, 0), ordered.get_sub_images())
            print ('Image loaded successfully!')
            ordered_created = True

        elif choice == 2:
            if not ordered_created:
                print('\nYou must load the ordered image first\n')
            else:
                image = misc.imread(input('Introduce the image full address: '))
                disordered = img.Image(image, ordered.get_rows(), ordered.get_cols())
                disordered.create_indexed_sub_images(ordered)
                initial_state = st.State(disordered.get_image_representation(), (-1, -1), disordered.get_sub_images())
                if disordered.compare_sub_images(ordered):
                    print ('Image loaded successfully, it matches!')
                    disordered_created = True
                else:
                    print('These images do not match, please insert a matching one.')

        elif choice == 3:

            if not ordered_created or not disordered_created:
                print('\nYou must load all images first\n')

            else:
                initial_time = 0
                solution = None
                problem = pr.Problem(goal_state, initial_state)
                strategy = input("""\nPlease choose strategy:
                                        BFS.
                                        DFS
                                        DLS
                                        IDS.
                                        UCS.\n""")

                if strategy == 'BFS':
                    initial_time = tm.time()
                    solution = problem.limited_search(strategy, 9999)

                elif strategy == 'DFS':
                    initial_time = tm.time()
                    solution = problem.limited_search(strategy, 999999)

                elif strategy == 'DLS':
                    initial_time = tm.time()
                    solution = problem.limited_search(strategy, int(input('Introduce a maximum depth: ')))

                elif strategy == 'IDS':
                    initial_time = tm.time()
                    solution = problem.search(strategy, 9999, int(input('Introduce a maximum Iteration: ')))

                elif strategy == 'UCS':
                    initial_time = tm.time()
                    solution = problem.limited_search(strategy, 9999)

                if solution:
                    create_solution(solution, strategy, tm.time() - initial_time)

        elif choice == 4:
            exit_program = True


def create_solution(current_node, strategy, elapsed_time):
    image = None
    total_depth = current_node.get_depth()
    total_cost = current_node.get_cost()
    file_name = 'output_' + strategy
    solution = []
    directory = file_name
    save_image = input('\nDo you want to store the images in output_' + strategy + ' folder? \n 1. Yes.\n 2. No.\n')

    if save_image == int(1):
        image = img.Image(None, 0, 0)

        if not os.path.exists(directory):
            os.makedirs(directory, mode=777)

        else:
            sh.rmtree(directory + '/*')

    while current_node.get_parent():
        movement = current_node.get_action()
        solution.append(movement)
        current_node = current_node.get_parent()

    with open(file_name, 'w') as f:
        f.write("Total Cost:: " + str(total_cost) + "\n")
        f.write("Final Depth: " + str(total_depth) + "\n")
        f.write("Elapsed time: " + str(elapsed_time) + "\n\n")
        f.write("Movements:" + "\n")

        for i in range(0, len(solution), 1):
            f.write(solution.pop() + '\n')
            if save_image == 1:
                    image.save_image(current_node, strategy)

        print('All files generated')

        f.close()

if __name__ == "__main__":
    main()