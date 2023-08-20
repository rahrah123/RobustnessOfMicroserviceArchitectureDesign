import networkx as nx
import math
import pandas as pd
import matplotlib.pyplot as plt
import pyperclip

def calculate_efficiency(G):
    if G.number_of_nodes() <= 1:
        return 0

    efficiency = 0

    for node in G.nodes():
        shortest_paths = nx.shortest_path_length(G, source=node)
        sigma = sum([1 / path_length for path_length in shortest_paths.values() if path_length > 0])
        efficiency += sigma

    return efficiency * (1 / (G.number_of_nodes() * (G.number_of_nodes() - 1)))

def calculate_vulnerability_function(G):
    degree_sum = 0

    for node in G.nodes():
        degree_sum += (G.degree(node) - ((2 * G.number_of_edges()) / G.number_of_nodes())) ** 2

    standard_deviation = degree_sum / len(G.nodes())
    return math.exp((math.sqrt(standard_deviation) / G.number_of_nodes()) + G.number_of_nodes() - G.number_of_edges() - 2 + (2 / G.number_of_nodes()))

def calculate_average_degree(G):
    degrees = [d for n, d in G.degree()]
    return sum(degrees) / len(G)

def calculate_average_squared_degree(G):
    degrees = [d for n, d in G.degree()]
    squared_degrees = [d ** 2 for d in degrees]
    return sum(squared_degrees) / len(G)

def calculate_critical_threshold(G):
    f = 1 - (1 / ((calculate_average_squared_degree(G) / calculate_average_degree(G)) - 1))
    return f

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
num_files = len(graphml_files)

df_rows = []

for graph_file in graphml_files:
    G = nx.read_graphml(graph_file)
    critical_threshold = calculate_critical_threshold(G)
    vulnerability_function = calculate_vulnerability_function(G)
    efficiency = calculate_efficiency(G)
    df_rows.append({
        "Graph File": graph_file,
        "Critical Threshold": f"{critical_threshold:.2f}",
        "Vulnerability Function": f"{vulnerability_function:.2e}",
        "Efficiency": f"{efficiency:.2f}"
    })

df = pd.DataFrame(df_rows)

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', fontsize=12)
for i, col in enumerate(df.columns):
    table[0, i].get_text().set_fontweight('bold')

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.2)

# Convert table data to text
table_text = ""
for row in df.values:
    table_text += "  ".join(str(cell) for cell in row)
    table_text += "\n"

# Copy table data to clipboard
pyperclip.copy(table_text)

plt.show()