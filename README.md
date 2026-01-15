# Projet DevOps 2026 - Convertisseur API

Ce projet est une API REST développée en Python (Flask) conteneurisée avec Docker. Elle inclut des pratiques DevOps complètes : CI/CD, Sécurité (SAST), et Observabilité.

## 🚀 Démarrage Rapide

### Prérequis
- Docker installé
- Python 3.9+

### 1. Lancer avec Docker
```bash
docker build -t devops-project .
docker run -p 5000:5000 devops-project
