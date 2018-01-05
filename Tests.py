import time
import collections as dq


class Node:

    def __init__(self, state, depth, action, parent, cost):
        self.state = state
        self.depth = depth
        self.action = action
        self.parent = parent
        self.cost = cost

    def stacks(self):
        pila = []
        times = []
        average = 0
        increase = 20000
        for i in range(1, 50, 1):
            start_time = time.time()
            for j in range(0, increase, 1):
                state = j
                depth = j
                action = j
                parent = j
                cost = j
                pila.append(Node(state, depth, action, parent, cost))
            while pila:
                pila.pop()
            increase += 20000
            average += (time.time() - start_time)
            times.append(time.time() - start_time)

        average /= 50
        biggest = times[0]
        smallest = times[0]

        for i in range(0,len(times),1):
            if times[i] > biggest:
                biggest = times[i]

            if times[i] < smallest:
                smallest = times[i]

        print ("\n\nSmallest time for Stacks: " + str(smallest) + "\nBiggest time for Stacks: " + str(biggest) +\
              "\nAverage for Stacks: " + str(average))

    def queues(self):
        cola = dq.deque()

        times = []
        average = 0
        increase = 20000
        for i in range(1, 50, 1):
            start_time = time.time()
            for j in range(0, increase, 1):
                state = j
                depth = j
                action = j
                parent = j
                cost = j
                cola.append(Node(state, depth, action, parent, cost))
            while cola:
                cola.popleft()

            increase += 20000
            average += (time.time() - start_time)
            times.append(time.time() - start_time)

        average /= 50
        biggest = times[0]
        smallest = times[0]

        for i in range(0, len(times), 1):
            if times[i] > biggest:
                biggest = times[i]

            if times[i] < smallest:
                smallest = times[i]

        print ("\n\nSmallest time for Queues: " + str(smallest) + "\nBiggest time for Queues: " + str(biggest) + \
                "\nAverage for Queues: " + str(average))


    def arrays(self):
        array = []
        times = []
        average = 0
        increase = 20000
        for i in range(1, 50, 1):
            start_time = time.time()
            for j in range(0, increase, 1):
                state = j
                depth = j
                action = j
                parent = j
                cost = j
                array.append(Node(state, depth, action, parent, cost))
            while array:
                array.pop()
            increase += 20000
            average += (time.time() - start_time)
            times.append(time.time() - start_time)

        average /= 50
        biggest = times[0]
        smallest = times[0]

        for i in range(0, len(times), 1):
            if times[i] > biggest:
                biggest = times[i]

            if times[i] < smallest:
                smallest = times[i]

        print ("\n\nSmallest time for Arrays: " + str(smallest) + "\nBiggest time for Arrays: " + str(biggest) + \
              "\nAverage for Arrays: " + str(average))

    def dictionaries(self):
        diccionario = {}
        times = []
        average = 0
        increase = 20000
        for i in range(1, 50, 1):
            start_time = time.time()
            for j in range(0, increase, 1):
                state = j
                depth = j
                action = j
                parent = j
                cost = j
                diccionario[j] = [Node(state, depth, action, parent, cost)]
            for j in range(0, increase, 1):
                del diccionario[j]

            increase += 20000
            average += (time.time() - start_time)
            times.append(time.time() - start_time)

        average /= 50
        biggest = times[0]
        smallest = times[0]

        for i in range(0, len(times), 1):
            if times[i] > biggest:
                biggest = times[i]

            if times[i] < smallest:
                smallest = times[i]

        print ("\n\nSmallest time for Dictionaries: " + str(smallest) + "\nBiggest time for Dictionaries: " + str(biggest) + \
              "\nAverage for Dictionaries: " + str(average))


    def main(self):
        jaja = Node(1,1,1,1,1)
        jaja.stacks()
        jaja.arrays()
        jaja.queues()
        jaja.dictionaries()

if __name__ == "__main__":
    jaja = Node(1,1,1,1,1)
    jaja.main()