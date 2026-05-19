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
        "KGF 2": 5,
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
        "Avengers 4": 3.5
    },


    "Kiran": {
        "KGF 2": 5,
        "Chhichhore": 4.5,
        "Barbie": 1,
        "Jab We Met": 2,
        "Avengers 4": 3.5
    },

    "Pooja": {
        "KGF 2": 1,
        "Chhichhore": 5,
        "Barbie": 3,
        "Jab We Met": 5,
        "Avengers 4": 2.5
    }
}

# -----------------------------------
# Create Graph
# -----------------------------------

G = nx.Graph()

# -----------------------------------
# Add User Nodes
# -----------------------------------

for user in users:

    G.add_node(
        user,
        bipartite=0,
        color="skyblue"
    )

# -----------------------------------
# Add Movie Nodes and Edges
# -----------------------------------

for user, movies in ratings.items():

    for movie, rating in movies.items():

        G.add_node(
            movie,
            bipartite=1,
            color="red"
        )

        G.add_edge(
            user,
            movie,
            weight=rating
        )

# -----------------------------------
# Add New User : Ashton Hall
# -----------------------------------

new_user = "Ashton Hall"

G.add_node(
    new_user,
    bipartite=0,
    color="yellow"
)

# -----------------------------------
# Calculate Total Movie Weights
# -----------------------------------

movie_scores = {}

for node in G.nodes():

    if node not in users and node != new_user:

        total_weight = 0

        for neighbor in G.neighbors(node):

            total_weight += G[node][neighbor]['weight']

        movie_scores[node] = total_weight

# -----------------------------------
# Find Top 2 Movies
# -----------------------------------

top_movies = sorted(
    movie_scores.items(),
    key=lambda x: x[1],
    reverse=True
)

top_2_movies = top_movies[:2]

# -----------------------------------
# Connect Ashton Hall to Top Movies
# -----------------------------------

for movie, score in top_2_movies:

    G.add_edge(
        new_user,
        movie,
        weight=score
    )

# -----------------------------------
# Calculate Node Sizes
# -----------------------------------

node_sizes = []

for node in G.nodes():

    # Existing Users
    if node in users:

        node_sizes.append(2500)

    # Ashton Hall
    elif node == new_user:

        node_sizes.append(3500)

    # Movies
    else:

        total_weight = 0

        for neighbor in G.neighbors(node):

            total_weight += G[node][neighbor]['weight']

        movie_size = total_weight * 200

        node_sizes.append(movie_size)

# -----------------------------------
# Node Colors
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

pos = nx.spring_layout(
    G,
    k=1.2,
    iterations=200,
    seed=42,
    weight='weight'
)

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
    font_color="black",
    font_weight='bold'
)

# -----------------------------------
# Draw Edge Labels
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
# Print Recommendations
# -----------------------------------

print("\nRecommended Movies for Ashton Hall:\n")

for movie, score in top_2_movies:

    print(movie, "-> Total Rating Score:", score)
