import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.id = str(uuid.uuid4())


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    heap = Node(arr[0])
    nodes = [heap]
    for i in range(1, n):
        parent_index = (i - 1) // 2
        parent_node = nodes[parent_index]

        if i % 2 == 0: 
            parent_node.left = Node(arr[i])
        else: 
            parent_node.right = Node(arr[i])
        nodes.append(parent_node.left if i % 2 == 0 else parent_node.right)

    return heap

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.key))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_binary_heap(heap):
    tree = nx.DiGraph()
    pos = {heap.id: (0, 0)}
    tree = add_edges(tree, heap, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

data = [10, 7, 8, 4, 6, 5, 2]

heap = build_heap(data)

draw_binary_heap(heap)