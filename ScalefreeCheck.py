import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import powerlaw

def is_scale_free(G):
    degree_sequence = [d for n, d in G.degree()]
    fit = powerlaw.Fit(degree_sequence)
    if fit.power_law.alpha:
        return float(fit.power_law.alpha)
    else:
        return False

graphml_files = ["graphs/spring-cloud-microservice.graphml", "graphs/spring-cloud-netflix.graphml", "graphs/spring-petclinic.graphml", "graphs/Tap-And-Eat-MicroServices.graphml", "graphs/Vehicle-Tracking.graphml", "graphs/Lakeside.graphml", "graphs/Microservices_book.graphml", "graphs/Open-loyalty.graphml", "graphs/EnterprisePlanner.graphml", "graphs/eShopOnContainers.graphml", "graphs/FTGO.graphml", "graphs/Robot_Shop.graphml", "graphs/ShareBike.graphml", "graphs/Spinnaker.graphml"]

table_data = []

for graphml_file in graphml_files:
    G = nx.read_graphml(graphml_file)
    num_nodes = G.number_of_nodes()

    dataset_fit = is_scale_free(G)

    G_barabasi = nx.barabasi_albert_graph(num_nodes, 4)

    barabasi_fit = is_scale_free(G_barabasi)

    table_data.append([graphml_file, dataset_fit, barabasi_fit])

# Create a DataFrame from the table data
df = pd.DataFrame(table_data, columns=['Graph Name', 'Dataset Fit', 'BA Fit'])

# Generate the table image plot
fig, ax = plt.subplots(figsize=(6, 4))
ax.axis('off')
tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)


# Save the table image plot
plt.savefig('table_image.png', bbox_inches='tight', pad_inches=0)

# Show the table image plot
plt.show()