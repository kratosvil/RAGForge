# RAGForge — Contexto de Desarrollo

## Estado actual
- **Stage activo:** Stage 1 — Core Hybrid RAG
- **Fase:** Inicio — estructura del proyecto no creada aún
- **Último punto de trabajo:** Lectura de README y ROADMAP. Proyecto vacío.

---

## Progreso por Stage

### Stage 1 — Core Hybrid RAG (Minikube)
- [ ] Scaffold de directorios y archivos base
- [ ] `requirements.txt` y `.env.example`
- [ ] Módulo ingestion: PDF parsing + limpieza + chunking
- [ ] Módulo embeddings: generación + caché
- [ ] Vector DB Pod (Chroma): despliegue en Minikube
- [ ] Módulo retriever: top-k + threshold
- [ ] Módulo generation: prompt template + LLM client
- [ ] RAGForge API Pod (FastAPI): endpoint `/query`
- [ ] Manifiestos k8s: namespace, deployments, services, ingress
- [ ] Test end-to-end dentro del cluster

### Stage 2 — Retrieval Optimization
- [ ] Pendiente (no iniciado)

### Stage 3 — Security & Hardening
- [ ] Pendiente (no iniciado)

### Stage 4 — Observability Layer
- [ ] Pendiente (no iniciado)

### Stage 5 — Infrastructure Integration
- [ ] Pendiente (no iniciado)

### Stage 6 — Production Deployment
- [ ] Pendiente (no iniciado)

---

## Decisiones técnicas tomadas

| Área | Decisión | Motivo |
|------|----------|--------|
| Vector DB | Por definir (Chroma o FAISS) | Pendiente de evaluar según persistencia en k8s |
| Embedding model | Por definir | Pendiente |
| LLM | API externa (por definir) | Sin GPU local |
| API framework | FastAPI | Definido en README |
| Cluster | Minikube | Definido en README |

---

## Dataset
- **Fuente:** https://kubernetes.io/docs/tutorials/kubernetes-basics/_print/
- **Formato:** PDF (~24 páginas)
- **Estado:** No descargado aún

---

## Notas técnicas
*(vacío — se irá llenando durante el desarrollo)*

---

## Próxima tarea
Crear scaffold completo del proyecto: estructura de directorios, `requirements.txt`, `.env.example`, `.gitignore`.
