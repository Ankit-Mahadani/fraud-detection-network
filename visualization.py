import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def build_graph(df):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row["sender"], row["receiver"], weight=row["amount"])
    return G

def visualize_graph(G, risk_score):
    pos = nx.spring_layout(G, seed=42)
    node_colors = [
        "red" if risk_score.get(n, 0) >= 0.6 else
        "orange" if risk_score.get(n, 0) >= 0.3 else
        "green"
        for n in G.nodes()
    ]
    edge_widths = [G[u][v]["weight"] / 2000 for u, v in G.edges()]

    plt.figure(figsize=(10, 7))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1200,
        edge_color="gray",
        width=edge_widths,
        font_size=10
    )
    plt.title("Transaction Network Visualization")
    plt.show()

def main():
    df = load_data("data/transactions.csv")
    G = build_graph(df)

    risk_score = {node: 0.2 for node in G.nodes()}
    visualize_graph(G, risk_score)

if __name__ == "__main__":
    main()
