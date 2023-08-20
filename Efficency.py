import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def calculate_efficiency (G):
    if G.number_of_nodes() <= 1:
        return 0

    efficiency = 0

    for node in G.nodes():
        shortest_paths = nx.shortest_path_length(G, source=node)
        sigma = sum([1 / path_length for path_length in shortest_paths.values() if path_length > 0])
        efficiency += sigma

    return efficiency * (1 / (G.number_of_nodes() * (G.number_of_nodes() - 1)))

graphml_files = [
    "graphs/spring-cloud-microservice.graphml",
    "graphs/spring-cloud-netflix.graphml",
    "graphs/spring-petclinic.graphml",
    "graphs/Tap-And-Eat-MicroServices.graphml",
    "graphs/Vehicle-Tracking.graphml",
    "graphs/Lakeside.graphml",
    "graphs/Microservices_book.graphml",
    "graphs/Open-loyalty.graphml",
    "graphs/EnterprisePlanner.graphml",
    "graphs/eShopOnContainers.graphml",
    "graphs/FTGO.graphml",
    "graphs/Robot_Shop.graphml",
    "graphs/ShareBike.graphml",
    "graphs/Spinnaker.graphml"
]

colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow', 'teal', 'lime']

plt.figure(figsize=(10, 6))

for i, graph_file in enumerate(graphml_files):
    G = nx.read_graphml(graph_file)
    destruction_percentages = np.linspace(0, 100, num=G.number_of_nodes()+1)
    averaged_shortest_paths_sums = np.zeros(len(destruction_percentages))
    for _ in range(100):     #simulation repeating times
        shortest_paths_sums = []
        for percentage in destruction_percentages:
            num_nodes_to_remove = int((percentage / 100) * G.number_of_nodes())
            nodes_to_remove = random.sample(list(G.nodes()), num_nodes_to_remove)
            G_temp = G.copy()
            G_temp.remove_nodes_from(nodes_to_remove)
            shortest_paths_sum = calculate_efficiency (G_temp)
            shortest_paths_sums.append(shortest_paths_sum)
        averaged_shortest_paths_sums += np.array(shortest_paths_sums)
    averaged_shortest_paths_sums /= 100  #average of simulation repeating times
    plt.plot(destruction_percentages, averaged_shortest_paths_sums, color=colors[i])

plt.xlabel("Destruction of Nodes (%)")
plt.ylabel("Average Efficiency")

legend_map = [graph_file.split('/')[-1].split('.')[0] for graph_file in graphml_files]
plt.legend(legend_map, loc='upper right')

plt.grid(True)
plt.show()