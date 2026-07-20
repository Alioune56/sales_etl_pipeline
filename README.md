# 📊 Sales ETL Pipeline

## 📌 Présentation

**Sales ETL Pipeline** est un projet de **Data Engineering** développé en Python ayant pour objectif de mettre en œuvre un pipeline **ETL (Extract – Transform – Load)** de bout en bout.

Le pipeline extrait des données de ventes à partir d'un fichier CSV, effectue les transformations nécessaires avec **Pandas**, puis charge les données nettoyées dans une base de données **PostgreSQL** grâce à **SQLAlchemy**.

Ce projet a été conçu en suivant les bonnes pratiques de développement logiciel : architecture modulaire, journalisation (logging), gestion de la configuration via des variables d'environnement et gestion des erreurs.

---

# 🏗️ Architecture du pipeline

```text
                 Fichier CSV
                      │
                      ▼
                📥 Extraction
               (extract.py)
                      │
                      ▼
             🔄 Transformation
            (transform.py)
      • Normalisation des colonnes
      • Suppression des doublons
      • Conversion des dates
      • Contrôle des données
                      │
                      ▼
               📤 Chargement
                 (load.py)
                      │
                      ▼
               🐘 PostgreSQL
```

---

# 📂 Structure du projet

```text
sales_etl_pipeline/
│
├── config/
│   ├── config.py
│   └── tables.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Technologies utilisées

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Logging
* Git
* GitHub
* Linux (Ubuntu)

---

# ✨ Fonctionnalités

Le pipeline permet de :

* Extraire les données depuis un fichier CSV
* Nettoyer et transformer les données
* Normaliser les noms des colonnes
* Supprimer les doublons
* Convertir automatiquement les colonnes de dates
* Contrôler les données manquantes
* Charger les données dans PostgreSQL
* Journaliser toutes les étapes du pipeline avec **logging**
* Gérer les paramètres de connexion grâce aux variables d'environnement

---

# 🚀 Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/Alioune56/sales_etl_pipeline.git
```

## 2. Accéder au projet

```bash
cd sales_etl_pipeline
```

## 3. Créer un environnement virtuel

```bash
python3 -m venv venv
```

## 4. Activer l'environnement

```bash
source venv/bin/activate
```

## 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

Créer un fichier `.env` à la racine du projet.

Exemple :

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sales_db
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
```

---

# ▶️ Exécution du pipeline

Lancer le pipeline :

```bash
python3 -m src.main
```

---

# 🔄 Fonctionnement du pipeline

Le pipeline suit les étapes suivantes :

1. 📥 Extraction des données depuis un fichier CSV.
2. 🔄 Transformation et nettoyage des données.
3. ✅ (Prochainement) Validation de la qualité des données.
4. 📤 Chargement des données dans PostgreSQL.
5. 📝 Génération des logs d'exécution.

---

# 📈 Évolutions prévues

Les prochaines améliorations du projet seront :

* Validation de la qualité des données (Data Quality)
* Modélisation d'un Data Warehouse
* Conteneurisation avec Docker
* Orchestration avec Apache Airflow
* Traitement distribué avec PySpark
* Tests unitaires avec Pytest
* Intégration continue (GitHub Actions)

---

# 🎯 Objectif du projet

Ce projet s'inscrit dans mon parcours de formation en **Data Engineering**. L'objectif est de mettre en pratique les concepts fondamentaux de l'ingénierie des données en développant un pipeline ETL modulaire, maintenable et évolutif, inspiré des bonnes pratiques utilisées en entreprise.

---

# 👨‍💻 Auteur

**Seydina Alioune Mboup**

Étudiant en Master 1 Intelligence Artificielle | Passionné par le Data Engineering

**GitHub :** https://github.com/Alioune56

**LinkedIn :** https://www.linkedin.com/in/seydina-alioune-mboup-504381230/
