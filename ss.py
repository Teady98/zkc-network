# Import necessary packages
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Set page title and introduction
st.title('Zachary\'s Karate Club Network Analysis')
st.markdown("""
Explore various metrics and visualizations of the Zachary's Karate Club network.
- **Graph Visualization:** Visualize the graph with nodes colored by their club membership.
- **Degree Distribution:** Histogram showing the distribution of node degrees.
- **Local Clustering Coefficients:** Display local clustering coefficients for each node.
- **Community Detection:** Detect communities using modularity optimization.
""")

# Load the ZKC graph
ZKC_graph = nx.karate_club_graph()

# Convert graph to NumPy array
A = nx.convert_matrix.to_numpy_array(ZKC_graph)

# Display the graph using NetworkX and Matplotlib
st.subheader('Graph Visualization')
fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.circular_layout(ZKC_graph)
nx.draw_networkx(ZKC_graph, pos, with_labels=False, node_color='skyblue', node_size=300, ax=ax)
ax.set_title('Karate Club Network')
st.pyplot(fig)

# Display node information
st.subheader('Node Information')
st.write(f"Number of nodes: {ZKC_graph.number_of_nodes()}")
st.write(f"Number of edges: {ZKC_graph.number_of_edges()}")

# Display degree distribution
degree = dict(ZKC_graph.degree())
degree_values = list(degree.values())
average_degree = np.mean(degree_values)
st.subheader('Degree Distribution')
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(degree_values, bins=range(max(degree_values)+1), alpha=0.7, label='Degree Distribution')
ax.axvline(average_degree, color='r', linestyle='dashed', linewidth=1, label='Average Degree')
ax.legend()
ax.set_xlabel('Degree')
ax.set_ylabel('Number of Nodes')
ax.set_title('Histogram of Node Degrees')
st.pyplot(fig)

# Display local clustering coefficient
local_clustering = nx.clustering(ZKC_graph)
average_clustering = nx.average_clustering(ZKC_graph)
st.subheader('Local Clustering Coefficients')
st.write("Node \t\t Clustering Coefficient")
for node, coeff in local_clustering.items():
    st.write(f"{node} \t\t {coeff:.3f}")
st.write(f"Average Clustering Coefficient: {average_clustering:.3f}")

# Perform community detection
communities = list(nx.algorithms.community.greedy_modularity_communities(ZKC_graph))
st.subheader('Community Detection')
st.write(f"Number of Communities Detected: {len(communities)}")
st.write("Community Information:")
for i, community in enumerate(communities):
    st.write(f"Community {i+1}: {sorted(community)}")

# Visualization of communities
st.subheader('Graph with Communities')
fig, ax = plt.subplots(figsize=(10, 8))
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i, community in enumerate(communities):
    nx.draw_networkx_nodes(ZKC_graph, pos, nodelist=community, node_color=colors[i % len(colors)], node_size=300, ax=ax)
nx.draw_networkx_edges(ZKC_graph, pos, ax=ax, alpha=0.5)
nx.draw_networkx_labels(ZKC_graph, pos, nx.get_node_attributes(ZKC_graph, 'club'), font_size=10, ax=ax)
ax.set_title('Karate Club Network with Communities')
st.pyplot(fig)

# Footer and credits
st.markdown("""
---

Created with Streamlit by Fatima Afzaal

[View on GitHub](https://github.com/yourusername/your-repo)
""")

# Display app
st.set_option('deprecation.showPyplotGlobalUse', False)  # Hide deprecated warning for st.pyplot()
st.sidebar.markdown("### About")
st.sidebar.info(
    "This web app analyzes the famous Zachary's Karate Club network, "
    "including graph visualization, degree distribution, local clustering coefficients, and community detection."
)
