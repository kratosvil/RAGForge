# 🚀 RAGForge – Kubernetes-Native Hybrid RAG Lab

RAGForge is a Kubernetes-native Hybrid Retrieval-Augmented Generation (RAG) system built using official Kubernetes documentation as a real-world technical corpus.

This project is designed with AI Infrastructure principles from day one:
- Container-first architecture
- Kubernetes deployment (Minikube for lab)
- Modular RAG design
- Production-ready mindset
- Observability-ready structure

---

# 🎯 Project Objective

Build a fully containerized Hybrid RAG system running on Kubernetes (Minikube) using:

📄 Official Kubernetes Basics Documentation  
Source:
https://kubernetes.io/docs/tutorials/kubernetes-basics/_print/

Initial Dataset:
Printable version (~24 pages)

Why start with this dataset?
- Controlled size
- Structured technical content
- DevOps-aligned domain
- Ideal for parameter tuning

---

# 🧠 Architecture Overview (Kubernetes-Native)

Flow:

User  
↓  
Ingress (Minikube)  
↓  
Service (ClusterIP / LoadBalancer)  
↓  
RAGForge API Pod (FastAPI)  
    ├── Retriever  
    ├── RAG Logic  
    └── LLM Client  
↓  
Vector DB Pod (Chroma / FAISS)  
↓  
External LLM API  

Observability (Optional – Stage 4+):
- Prometheus
- Grafana
- Structured Logging

---

# ☸️ Why Kubernetes From Day One?

- Clean isolation from local OS
- Portability across environments
- Easy scaling (HPA later)
- Future-ready production design
- Strong alignment with AI Infra / MLOps roles

Minikube provides:
- Local cluster
- Safe experimentation
- No pollution of host system
- Real Kubernetes workflow

---

# 📂 Project Structure

ragforge/
│
├── README.md
├── ROADMAP.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│ ├── raw/
│ │ └── kubernetes_basics.pdf
│ └── processed/
│
├── src/
│ ├── ingestion/
│ ├── embeddings/
│ ├── retriever/
│ ├── generation/
│ ├── evaluation/
│ └── config/
│
├── k8s/
│ ├── namespace.yaml
│ ├── ragforge-deployment.yaml
│ ├── ragforge-service.yaml
│ ├── vector-db-deployment.yaml
│ ├── vector-db-service.yaml
│ └── ingress.yaml
│
└── tests/


---

# 🧩 Core Modules

## 1️⃣ Ingestion

- Extract text from PDF
- Clean formatting artifacts
- Normalize text
- Remove duplicated headers
- Section-aware chunking

Key Parameters:
- chunk_size
- chunk_overlap
- section tagging
- page metadata

---

## 2️⃣ Embeddings

- Generate vector representations
- Batch processing
- Cache embeddings
- Normalize vectors

Key Concepts:
- Cosine similarity
- Embedding dimensionality
- Semantic proximity

---

## 3️⃣ Retriever

- Top-K similarity search
- Similarity threshold filtering
- Metadata filtering
- Section-aware retrieval

Why:
Retrieval precision > model size.

---

## 4️⃣ Generation

- Grounded prompt template
- Context injection
- Citation enforcement
- Anti-hallucination rules

Security:
- Prompt injection mitigation
- Input validation
- Context isolation

---

## 5️⃣ Evaluation

Metrics:
- Context relevance
- Faithfulness
- Latency
- Token usage

MLOps mindset from start.

---

# 🔐 Security Best Practices

- No secrets in Git
- `.env` excluded
- Kubernetes secrets for API keys
- Input length control
- Prompt injection mitigation
- Mandatory citation policy

---

# ⚙️ Configurable Parameters

| Parameter | Impact |
|------------|----------|
| chunk_size | Retrieval granularity |
| chunk_overlap | Context continuity |
| top_k | Retrieval depth |
| similarity_threshold | Noise filtering |
| temperature | Determinism |
| max_tokens | Cost control |
| embedding_model | Vector quality |

---

# 🚀 Running on Minikube

1. Start Minikube
2. Build Docker image
3. Apply namespace
4. Deploy vector DB
5. Deploy RAGForge API
6. Expose via Ingress
7. Query via browser / curl

This simulates a real production deployment workflow.

---

# 🔮 Future Expansion

- Hybrid Search (BM25 + Vector)
- Re-ranking layer
- HPA autoscaling
- Prometheus metrics export
- Grafana dashboards
- CI/CD with GitHub Actions
- Helm chart
- Multi-environment setup (dev/stage/prod)

---

# 🎯 Engineering Outcome

After completion, this project demonstrates:

- Kubernetes-native AI system design
- Hybrid RAG architecture
- AI Infrastructure thinking
- Observability awareness
- Production-oriented DevOps skills

Target Roles:
AI Infrastructure Engineer  
MLOps Engineer  
LLMOps Engineer  
Platform Engineer (AI Focus)