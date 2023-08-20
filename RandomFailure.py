import networkx as nx
import matplotlib.pyplot as plt
import random

def destroy_nodes_and_giant_component_size(graph, graph_name, color):
    if graph.number_of_nodes() == 0:
        return

    num_nodes = graph.number_of_nodes()

    percentages = []
    giant_component_sizes = []

    num_simulations = 100

    for i in range(num_nodes + 1):
        giant_component_size_sum = 0

        for _ in range(num_simulations):
            destroyed_graph = graph.copy()
            destroyed_nodes = random.sample(list(graph.nodes()), i)
            destroyed_graph.remove_nodes_from(destroyed_nodes)

            components = list(nx.connected_components(destroyed_graph))
            giant_component_size = 0

            if components:
                largest_component = max(components, key=len)
                giant_component_size = len(largest_component)

            giant_component_size_sum += giant_component_size

        percentage_destroyed = i / num_nodes * 100
        average_giant_component_size = giant_component_size_sum / num_simulations

        percentages.append(percentage_destroyed)
        giant_component_sizes.append(average_giant_component_size)

    plt.plot(percentages, giant_component_sizes, marker='o', label=graph_name, color=color)


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

plt.figure(figsize=(10, 6))

for i, graph_file in enumerate(graphml_files):
    G = nx.read_graphml(graph_file)
    G_undirected = G.to_undirected()
    color = plt.cm.get_cmap("tab20")(i / len(graphml_files))
    destroy_nodes_and_giant_component_size(G_undirected, graph_file, color)

plt.xlabel("Destruction of Nodes (%)")
plt.ylabel("Size of Giant Component")
plt.grid(True)
plt.legend()
plt.show()