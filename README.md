# Fraud Detection Using Transaction Network

## Overview
This project implements a graph-based fraud detection system by modeling financial transactions as a network. Each account is represented as a node and each transaction is represented as a directed edge with an associated transaction amount.

By analyzing transaction patterns such as circular money flow, high outgoing transaction values, and highly connected accounts, the system identifies potentially fraudulent behavior in an explainable and visual manner.

---

## Problem Statement
Financial fraud often involves complex transaction structures that are difficult to detect using traditional methods. Common fraud patterns include circular transactions, abnormal fund transfers, and coordinated activity among multiple accounts.

This project aims to detect such patterns using network analysis and graph theory.

---

## Features
- Builds a directed transaction network from CSV data  
- Detects circular transaction patterns (cycles)  
- Flags accounts with high outgoing transaction amounts  
- Assigns a risk score to each account  
- Visualizes the transaction network with risk-based coloring  

---

## Technologies Used
- Python  
- Pandas  
- NetworkX  
- Matplotlib  

---

## Project Structure
```text
fraud-detection-network/
│
├── data/
│ └── transactions.csv
├── fraud_detection.py
├── visualization.py
├── requirements.txt
└── README.md
```


---

## Dataset
The dataset is stored in CSV format at:


### CSV Format
```csv
sender,receiver,amount
A,B,5000
B,C,4800
C,A,4700
```
How to Run
1. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run Fraud Detection
```bash
python fraud_detection.py
```

This will:
1. Analyze the transaction network
2. Print suspicious accounts and detected cycles
3. Display a network visualization

3. (Optional) Run Visualization Only
```bash
python visualization.py
```

## Output
1. Console output showing suspicious accounts and transaction cycles
2. Graph visualization where:
  a. Green nodes indicate low-risk accounts
  b. Orange nodes indicate medium-risk accounts
  c. Red nodes indicate high-risk accounts

## Innovation
The innovation of this project lies in its explainable, rule-based fraud detection approach. Instead of relying on black-box machine learning models, it uses graph-based analysis to provide transparent and interpretable fraud detection, supported by visual insights.

## Conclusion
This project demonstrates how network analysis and graph theory can be effectively applied to real-world financial fraud detection scenarios, providing both analytical and visual understanding of suspicious transaction behavior.
