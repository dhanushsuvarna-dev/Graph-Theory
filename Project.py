import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------------
# Users
# -----------------------------------

users = [
    "Arjun",
    "Rahul",
    "Neha",
    "Kiran",
    "Pooja"
]

# -----------------------------------
# Movie Ratings Dataset
# -----------------------------------

ratings = {

    "Arjun": {
        "KGF 2": 5,
        "Chhichhore": 4,
        "Barbie": 2,
        "Jab We Met": 3,
        "Avengers 4": 4.5
    },

    "Rahul": {
        "KGF 2": 3,
        "Chhichhore": 4,
        "Barbie": 3,
        "Jab We Met": 5,
        "Avengers 4": 4
    },

    "Neha": {
        "KGF 2": 4,
        "Chhichhore": 3,
        "Barbie": 4,
        "Jab We Met": 3.5,
        "Avengers 4": 4.5
    },

    "Kiran": {
        "KGF 2": 3,
        "Chhichhore": 4.5,
        "Barbie": 1,
        "Jab We Met": 2,
        "Avengers 4": 5
    },

    "Pooja": {
        "KGF 2": 1,
        "Chhichhore": 5,
        "Barbie": 3,
        "Jab We Met": 5,
        "Avengers 4": 4.5
    }
}

# -----------------------------------
# Create Graph
# -----------------------------------

G = nx.Graph()

# Add user nodes
for user in users:
    G.add_node(
        user,
        bipartite=0,
        color="skyblue"
    )

# Add movie nodes and weighted edges
for user, movies in ratings.items():

    for movie, rating in movies.items():

        # Add movie node
        G.add_node(
            movie,
            bipartite=1,
            color="red"
        )

        # Add edge with rating weight
        G.add_edge(
            user,
            movie,
            weight=rating
        )

# -----------------------------------
# Calculate Node Sizes
# -----------------------------------

node_sizes = []

for node in G.nodes():

    # Large fixed size for users
    if node in users:

        node_sizes.append(2500)

    # Movie size based on total edge weight
    else:

        total_weight = 0

        for neighbor in G.neighbors(node):

            total_weight += G[node][neighbor]['weight']

        # Scale node size
        movie_size = total_weight * 200

        node_sizes.append(movie_size)

# -----------------------------------
# Graph Colors
# -----------------------------------

node_colors = []

for node in G.nodes():

    node_colors.append(
        G.nodes[node]['color']
    )

# -----------------------------------
# Graph Layout
# -----------------------------------

plt.figure(figsize=(16, 10))

pos = nx.bipartite_layout(G, users)

# -----------------------------------
# Draw Graph
# -----------------------------------

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=node_sizes,
    font_size=9,
    font_weight='bold'
)

# -----------------------------------
# Draw Edge Labels (Ratings)
# -----------------------------------

edge_labels = nx.get_edge_attributes(
    G,
    'weight'
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=8
)

# -----------------------------------
# Title
# -----------------------------------

plt.title(
    "Graph Based Movie Recommendation System",
    fontsize=16
)

plt.show()

# -----------------------------------
# Recommendation Logic
# -----------------------------------

print("\nMovie Recommendations:\n")

for user in users:

    watched_movies = set(
        ratings[user].keys()
    )

    recommendations = []

    for other_user in users:

        if other_user != user:

            other_movies = set(
                ratings[other_user].keys()
            )

            # Find common movies
            common_movies = watched_movies.intersection(
                other_movies
            )
