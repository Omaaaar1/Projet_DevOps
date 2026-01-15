🚀 Projet DevOps 2026 - API de Conversion

Ce projet est une démonstration complète d'un cycle de vie DevOps moderne. Il s'agit d'un microservice RESTful développé en Python (Flask) qui effectue des conversions d'unités, tout en intégrant les meilleures pratiques : CI/CD, Conteneurisation, Orchestration, Sécurité et Observabilité.

📑 Table des Matières

Fonctionnalités

Architecture Technique

Prérequis

Installation et Démarrage

Localement (Python)

Avec Docker

Avec Kubernetes

Observabilité & Métriques

Pipeline CI/CD

🌟 Fonctionnalités

L'API expose les endpoints suivants :

Méthode

Endpoint

Description

Exemple

GET

/

Vérification du statut (Healthcheck)

curl http://localhost:5000/

GET

/convert

Convertit Celsius en Fahrenheit

curl http://localhost:5000/convert?celsius=25

GET

/metrics

Métriques Prometheus (Monitoring)

curl http://localhost:5000/metrics

🛠 Architecture Technique

Langage : Python 3.9 (Framework Flask)

Container : Docker (Image optimisée python:3.9-slim)

Orchestration : Kubernetes (Manifestes de déploiement inclus)

CI/CD : GitHub Actions (Build, Test, Scan de sécurité)

Sécurité : Bandit (Analyse statique SAST)

Monitoring : Prometheus Client (Logs structurés et métriques personnalisées)

📋 Prérequis

Docker Desktop installé.

Python 3.9+ (Optionnel si utilisation de Docker).

Git.

🚀 Installation et Démarrage

1. Lancement Local (Python)

Idéal pour le développement rapide.

# Cloner le dépôt
git clone [https://github.com/Omaaaar1/Projet_DevOps.git](https://github.com/Omaaaar1/Projet_DevOps.git)
cd Projet_DevOps

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py


Accès : http://localhost:5000

2. Lancement avec Docker

Pour garantir un environnement isolé et reproductible.

# Construire l'image Docker
docker build -t devops-project .

# Lancer le conteneur (Port 5000)
docker run -p 5000:5000 devops-project


3. Déploiement Kubernetes

Pour simuler un déploiement en production (nécessite Minikube ou Kind).

# Appliquer la configuration de déploiement et de service
kubectl apply -f k8s/deployment.yaml

# Vérifier les pods
kubectl get pods

# (Sur Minikube) Obtenir l'URL d'accès
minikube service devops-project-service


📊 Observabilité & Métriques

L'application est conçue pour être surveillée ("Observable").

Logs Structurés : Chaque requête génère un log incluant un TraceID unique pour faciliter le débogage.

Prometheus : L'endpoint /metrics expose des données en temps réel :

app_requests_total : Nombre total de requêtes HTTP.

process_cpu_seconds_total : Utilisation CPU.

🛡 Pipeline CI/CD et Sécurité

Ce projet utilise GitHub Actions pour automatiser la qualité du code. Le fichier de configuration se trouve dans .github/workflows/pipeline.yml.

À chaque push sur la branche main, le pipeline exécute :

Installation de l'environnement Python.

Scan de Sécurité (SAST) avec bandit pour détecter les vulnérabilités (injection, crypto faible, etc.).

Build Docker pour vérifier que le Dockerfile est valide.

👥 Mainteneurs

[RjabOmar] - Lead Developer & DevOps Engineer