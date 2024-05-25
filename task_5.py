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
        self.visited = False 
        self.visit_color = None 
        
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.key))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree, colors=None):
    graph = nx.DiGraph()
    pos = {node.id: (0, 0) for node in tree}
    graph = add_edges(graph, tree, pos)

    if colors is None:
        colors = [node.color for node in tree]
    labels = {node.id: str(node.key) for node in tree}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()       

def dfs(root, colors, step=0):
    if root is None:
        return

    root.visited = True
    root.visit_color = rgb_to_hex(step)
    colors[root.id] = root.visit_color

    dfs(root.left, colors, step + 1)
    dfs(root.right, colors, step + 1)

def bfs(root, colors):
    queue = [root]

    while queue:
        node = queue.pop(0)
        node.visited = True
        node.visit_color = rgb_to_hex(len(queue))
        colors[node.id] = node.visit_color

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)        
            
def rgb_to_hex(step):
    
    r = (step % 16) * 16
    g = (step // 16) % 16 * 16
    b = (step // 256) * 16
    return f"#{r:02x}{g:02x}{b:02x}"

heap = Node(10)
heap.left = Node(7)
heap.left.left = Node(4)
heap.left.right