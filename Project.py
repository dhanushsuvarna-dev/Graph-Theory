import networkx as nx
import matplotlib.pyplot as plt

# -------------------------------
# Users
# -------------------------------
users = ["Arjun", "Rahul", "Neha", "Aisha", "Kiran", "Pooja"]

# -------------------------------
# Movie Ratings Dataset
# -------------------------------
ratings = {
    "Arjun": {
        "KGF 2": 5,
        "Interstellar": 5,
        "John Wick": 5,
        "Inception": 5,
        "Avengers Endgame": 5
    },

    "Rahul": {
        "KGF 2": 5,
        "Animal": 5,
        "Chhichhore": 5,
        "Spider-Man NWH": 5,
        "Kalki 2898 AD": 5
    },

    "Neha": {
        "YJHD": 5,
        "Barbie": 5,
        "Jab We Met": 5,
        "ZNMD": 5,
        "Your Name": 5
    },

    "Aisha": {
        "Little Women": 5,
        "Barbie": 5,
        "Interstellar": 5,
        "Your Name": 5,
        "Dune": 5
    },

    "Kiran": {
        "Interstellar": 5,
        "Inception": 5,
        "Dune": 5,
        "The Matrix": 5,
        "Spider-Verse": 5
    },

    "Pooja": {
        "3 Idiots": 5,
        "Spider-Man NWH": 5,
        "ZNMD": 5,
        "Chhichhore": 5,
        "Your Name": 4
    }
}

# -------------------------------
# Create Bipartite Graph
# -------------------------------
G = nx.Graph()

# Add user nodes
for user in users:
    G.add_node(user, bipartite=0, color='lightblue')

# Add movie nodes and edges
for user, movies in ratings.items():
    for movie, rating in movies.items():

        G.add_node(movie, bipartite=1, color='lightgreen')

        # Edge between user and movie
        G.add_edge(user, movie, weight=rating)

# -------------------------------
# Draw Graph
# -------------------------------
colors = [G.nodes[node]['color'] for node in G.nodes()]

plt.figure(figsize=(14, 10))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=2000,
    font_size=8
)

# Edge labels (ratings)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)

plt.title("Movie Recommendation Graph")
plt.show()

# -------------------------------
# Simple Recommendation Logic
# -------------------------------
print("\nMovie Recommendations:\n")

for user in users:

    watched = set(ratings[user].keys())

    recommendations = []

    for other_user in users:

        if other_user != user:

            other_movies = set(ratings[other_user].keys())

            common_movies = watched.intersection(other_movies)

            # If users have common interests
            if len(common_movies) >= 2:

                recommended = other_movies - watched

                recommendations.extend(recommended)

    recommendations = list(set(recommendations))

    print(user, "->", recommendations)
