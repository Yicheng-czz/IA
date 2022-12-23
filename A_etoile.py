from util import *

# h(n) and name
nodes_List = [[10, "S"], [2, "A"], [5, "B"], [2, "C"], [1, "D"], [0, "G"]]

matrix = np.matrix([
    [0, 2, 3, -1, 5, -1],
    [2, 0, -1, 4, -1, -1],
    [3, -1, 0, -1, 4, -1],
    [-1, 4, -1, 0, -1, 2],
    [4, -1, 4, -1, 0, 5],
    [-1, -1, -1, 2, 5, 0]
])

if __name__ == '__main__':
    num = int(input("Nombre des noeuds: "))

    # 边缘
    FRINGE = PriorityQueue()
    FRINGE.append_elem("S", Node(8, "S", 0, 0))

    # 当前点 访问过的点
    CLOSED = []
    # le noeud suivant
    node_current = []
    index = 0
    expanded_node = []
    circuit = ""
    flag = False

    while True:
        node_current = FRINGE.get_head()
        index = node_current[1].get_index()
        current_g = node_current[1].get_g()
        print("node_current:" + node_current[1].get_name())

        if node_current[1].get_name() == "G":
            print("Goal")
            break

        print("can go: ")

        # 扩展队列头节点
        for i in range(0, num):
            # 不是自己  而且  不在CLOSED中
            if matrix[index, i] > 0:
                if not Is_elem_inCLOSED(CLOSED, i):
                    flag = True
                    print(" " + nodes_List[i][1] + " ")
                    FRINGE.append_elem(node_current[1].get_name(),
                                       Node(nodes_List[i][0], nodes_List[i][1], i, current_g + matrix[index, i]))

        # si 'node_current' a des successors
        if flag:
            CLOSED.append(node_current)
            expanded_node.append(node_current[1].get_name())
            flag = False

        FRINGE.watch_queue()

    expanded_node.append("G")
    print("nodes expanded: ",expanded_node)
    print("circuit réel: ", recuperer_circuit(CLOSED))
