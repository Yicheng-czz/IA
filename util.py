import numpy as np

# construire une class 'Node' pour stocker des propriétés
class Node:
    def __init__(self, node_h, node_name, node_index, node_g):
        self.__node_name = node_name
        self.__node_index = node_index
        self.__node_h = node_h
        self.__node_g = node_g

    def get_h(self):
        return self.__node_h

    def get_name(self):
        return self.__node_name

    def get_g(self):
        return self.__node_g

    def get_index(self):
        return self.__node_index

# construire une structure de donnée 'PriorityQueue'
class PriorityQueue:
    def __init__(self):
        self.__queue = []

    # lister tous les f() de la liste 'FRINGE'
    def get_f_list(self):
        f_list = []
        for i in self.__queue:
            f_list.append(i[1].get_g() + i[1].get_h())
        return f_list

    # ici, le format de 'element' doit [index,g,h]
    def append_elem(self, node_current, node):
        f = node.get_h() + node.get_g()
        f_list = self.get_f_list()

        if len(self.__queue) == 0:
            self.__queue.append([node_current, node])
        elif f >= f_list[-1]:
            self.__queue.append([node_current, node])
        else:
            for i in range(0, len(f_list)):
                # if current_f < i_f
                if f < f_list[i]:
                    self.__queue.insert(i, [node_current, node])
                    break

    # obtenir la tête de 'PriorityQueue' et la supprimer de 'PriorityQueue'
    def get_head(self):
        if len(self.__queue) == 0:
            return None
        else:
            head = self.__queue[0]
            self.__queue.remove(head)
            return head

    # obtenir seulement g() de la tête de 'PriorityQueue'
    def get_head_g(self):
        return self.__queue[0][1].get_g()

    def Is_elem_inQueue(self, elem_index):
        if len(self.__queue) == 0:
            return False
        for i in self.__queue:
            if elem_index == i[1].get_index():
                return True
            else:
                return False

    # Parcours 'PriorityQueue'
    def watch_queue(self):
        for i in self.__queue:
            print(i[1].get_name() + " : " + str(i[1].get_index()) + " " + str(i[1].get_g()) + " " + str(i[1].get_h()))


# numberNode should be a Node list
def graph(NodeList):
    i = 0
    # initialiser le graphe
    matrix = np.zeros((len(NodeList), len(NodeList)))

    while i < len(NodeList):
        j = i + 1
        while j < len(NodeList):
            matrix[i][j] = matrix[j][i] = input(
                NodeList[i].get_name() + " à " + NodeList[j].get_name() + " égale à [g(n)]: ")
            j = j + 1
        i = i + 1

    return matrix


# juger si 'elem_index' il est dans 'CLOSED'
def Is_elem_inCLOSED(CLOSED, elem_index):
    if len(CLOSED) == 0:
        return False
    for i in CLOSED:
        if i[1].get_index() == elem_index:
            return True
    return False


# recuperer le circuit reel à travers list 'CLOSED'
def recuperer_circuit(CLOSED):
    circuit = [CLOSED[-1][1].get_name(),"G"]
    parent = CLOSED[-1][0]
    for i in range(len(CLOSED) - 2, -1, -1):
        if parent == CLOSED[i][1].get_name():
            circuit.insert(0,parent)
            parent = CLOSED[i][0]
            if parent == "S":
                circuit.insert(0,"S")
                break

    return circuit
