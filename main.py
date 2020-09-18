####### BFS SOLUTION ########
from make_states import make_states
import graph_operation as go

graph = {}
states_count = 0
child_count = 0
possible_path = []

def add_node(i, parent, x, y):
    '''
    Denoteing each node child
    params : current capacity in A, current capacity in B, previous related node
    '''
    global states_count, child_count, possible_path
    parent_node = [x, y]
    node_list = set()

    init = i

    # Generateing the nodes
    node_list.add(instance.fillA(parent_node[0], parent_node[1]))
    node_list.add(instance.fillB(parent_node[0], parent_node[1]))
    node_list.add(instance.pourBtoA(parent_node[0], parent_node[1]))
    node_list.add(instance.pourAtoB(parent_node[0], parent_node[1]))
    node_list.add(instance.emptyA(parent_node[0], parent_node[1]))
    node_list.add(instance.emptyB(parent_node[0], parent_node[1]))

    # Removing unwanted
    if (0,0) in node_list:
        node_list.remove((0,0))
    if (parent_node[0], parent_node[1]) in node_list:
        node_list.remove((parent_node[0], parent_node[1]))

    parent_node = [init, parent, x, y]

    # Cleaning list
    final_node_list = list()
    for x in node_list:
        x = list(x)
        i = i + 1
        child_count = child_count + 1
        x.insert(0, child_count)
        x.insert(1, init)
        final_node_list.append(x)

    # Adding to the Graph
    graph[str(list(parent_node))] = final_node_list 

    # print("No of " + str(list(parent_node)) + " child = " + str(len(list(node_list))))
    states_count = states_count + len(final_node_list )

def create_graph(x,y):
    add_node(0,'null', x, y)
    current_node = str([0,'null',x,y])
    visited = list()
    visited.append(current_node)
    k = 0
    for node in visited:
        for states in graph[node]:
            add_node(states[0], states[1], states[2], states[3])
            new_node = str([states[0], states[1], states[2], states[3]])
            if new_node not in visited:
                visited.append(str([states[0], states[1], states[2], states[3]]))
        if k == 256:
            break
        k = k + 1
        
def trace_path(parent_id):
    for x in graph:
        for x in graph[x]:
            if x[0] is parent_id:
                print('(',x[2],',',x[3],')', end= '<-')
                trace_path(x[1])

def print_graph():
    n=0
    for x in graph:
        #print(str(x) + " - " + str(graph[x]))
        for x in graph[x]:
            if x[2] == 2:
                print('(',x[2],',',x[3],')', end= '<-')
                trace_path(x[1])
                print('(',0,',',0,')', end= '\n')
                n = n + 1
                #print("Found")
    print("Total No of States = ", str(states_count), " And A=2 are ", n)

if __name__ == '__main__':
    A = 4
    B = 3
    x = 0
    y = 0
    desired_x = 2
    desired_y = 0
    
    instance = make_states(A, B)
    create_graph(x,y)
    print_graph()
    # start = str([0,0])
    # print(go.bfs(graph, start))