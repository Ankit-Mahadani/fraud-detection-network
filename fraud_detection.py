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

def detect_fraud(G, amount_threshold=5000):
    risk_score = {node: 0 for node in G.nodes()}

    for node in G.nodes():
        outgoing_amount = sum(G[node][nbr]["weight"] for nbr in G.successors(node))
        if outgoing_amount > amount_threshold:
            risk_score[node] += 0.4

    cycles = list(nx.simple_cycles(G))
    for cycle in cycles:
        for node in cycle:
            risk_score[node] += 0.4

    for node, degree in G.degree():
        if degree > 3:
            risk_score[node] += 0.2

    return risk_score, cycles

def visualize_graph(G, risk_score):
    pos = nx.spring_layout(G, seed=42)
    node_colors = [
        "red" if risk_score[n] >= 0.6 else
        "orange" if risk_score[n] >= 0.3 else
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
    plt.title("Fraud Detection using Transaction Network")
    plt.show()

def main():
    df = load_data("data/transactions.csv")
    G = build_graph(df)
    risk_score, cycles = detect_fraud(G)

    print("Suspicious Accounts (Risk Score ≥ 0.6):")
    for node, score in risk_score.items():
        if score >= 0.6:
            print(f"{node} -> Risk Score: {score}")

    print("\nDetected Transaction Cycles:")
    for cycle in cycles:
        print(" -> ".join(cycle))

    visualize_graph(G, risk_score)

if __name__ == "__main__":
    main()
