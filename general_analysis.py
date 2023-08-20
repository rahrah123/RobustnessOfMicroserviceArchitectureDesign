import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def calculate_general_analysis(G):


    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    avg_degree = round(calculate_average_degree(G), 3)
    clustering_coefficient = round(nx.average_clustering(G), 3)

    return {
        "Number of Nodes": num_nodes,
        "Number of Edges": num_edges,
        "Average Degree": avg_degree,
        "Clustering Coefficient": clustering_coefficient
    }

def calculate_average_degree(G):
    degrees = [d for n, d in G.degree()]
    return sum(degrees) / len(G)

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

df_rows = []

for graph_file in graphml_files:
    G = nx.read_graphml(graph_file)
    metrics = calculate_general_analysis(G)
    if metrics is not None:
        metrics["Graph File"] = graph_file
        df_rows.append(metrics)

df = pd.DataFrame(df_rows)

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', fontsize=12)
for i, col in enumerate(df.columns):
    table[0, i].get_text().set_fontweight('bold')

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.2)
plt.show()



# Export DataFrame to Excel
df.to_excel("output2.xlsx", index=False)