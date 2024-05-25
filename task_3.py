import heapq

class Node:
    def __init__(self, value, distance):
        self.value = value
        self.distance = distance

class Graph:
    def __init__(self):
        self.vertices = {} 

    def add_vertex(self, value):
        self.vertices[value] = []

    def add_edge(self, source, destination, weight):
        self.vertices[source].append((destination, weight))

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0

        pq = [] 
        heapq.heappush(pq, (0, start))  

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue  

            for neighbor, edge_weight in self.vertices[current_vertex]:
                new_distance = current_distance + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

        return distances 

graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B', 7)
graph.add_edge('A', 'C', 9)
graph.add_edge('A', 'D', 'infinity')  
graph.add_edge('B', 'C', 10)
graph.add_edge('B', 'D', 15)
graph.add_edge('C', 'D', 11)
graph.add_edge('C', 'E', 2)
graph.add_edge('D', 'E', 6)

start = 'A'

distances = graph.dijkstra(start)
print("Найкоротші шляхи від", start)
for vertex, distance in distances.items():
    if distance != float('inf'):
        print(f"{start} -> {vertex}: {distance}")
    else:
        print(f"{start} -> {vertex}: Немає шляху")