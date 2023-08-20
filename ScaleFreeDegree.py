import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


graphml_files = ["graphs/spring-cloud-microservice.graphml","graphs/spring-cloud-netflix.graphml","graphs/spring-petclinic.graphml","graphs/Tap-And-Eat-MicroServices.graphml","graphs/Vehicle-Tracking.graphml","graphs/Lakeside.graphml","graphs/Microservices_book.graphml","graphs/Open-loyalty.graphml","graphs/EnterprisePlanner.graphml","graphs/eShopOnContainers.graphml","graphs/FTGO.graphml","graphs/Robot_Shop.graphml","graphs/ShareBike.graphml","graphs/Spinnaker.graphml"]
num_files = len(graphml_files)
fig, axs = plt.subplots(num_files, 2, figsize=(8, 10 * num_files))

for i, graphml_file in enumerate(graphml_files):
    G = nx.read_graphml(graphml_file)
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(degree_sequence)
    #Degree distribution
    axs[i, 0].plot(degree_sequence, color='black', linestyle='-', marker='o')
    axs[i, 0].set_title("Degree Distribution Plot - {}".format(graphml_file))
    axs[i, 0].set_ylabel("Degree")
    axs[i, 0].set_xlabel("Node Count")
    # Degree histogram
    axs[i, 1].bar(*np.unique(degree_sequence, return_counts=True), color='black')
    axs[i, 1].set_title("Degree Histogram - {}".format(graphml_file))
    axs[i, 1].set_xlabel("Degree")
    axs[i, 1].set_ylabel("Node Count")

plt.subplots_adjust(hspace=1.5)

plt.show()