# Prototype IA – Génération d’un plan de remédiation

## Description

Ce projet présente un prototype permettant de transformer automatiquement des constats techniques issus d’un audit en un plan de remédiation structuré.

Le prototype analyse les constats, les priorise selon leur criticité, propose des actions correctives, estime la charge de travail et génère un backlog ainsi qu’une feuille de route (roadmap).

---

## Objectifs

Le prototype permet de :

- Analyser les constats techniques d'un audit.
- Identifier les problèmes prioritaires.
- Déterminer le niveau de criticité.
- Proposer des actions correctives.
- Générer automatiquement un backlog.
- Estimer la charge de travail (jours/homme).
- Identifier les dépendances entre les tâches.
- Construire une roadmap de remédiation.

---

## Technologies utilisées

- Python 3
- Pandas
- OpenPyXL (export CSV/Excel)

---

## Structure du projet

```
IA_Remediation/
│
├── data/
│   └── audit.csv
│
├── output/
│   ├── summary.txt
│   ├── remediation_plan.csv
│   ├── backlog.csv
│   └── roadmap.csv
│
├── app.py
├── ai_engine.py
├── prompt.txt
├── requirements.txt
└── README.md
```

---

## Données d'entrée

Le fichier `audit.csv` contient les constats techniques identifiés lors d’un audit.

Chaque ligne représente un problème détecté avec les informations suivantes :

- ID
- Catégorie
- Constat
- Description
- Composant concerné
- Dépendance éventuelle
- Statut

---

## Résultats générés

Le programme génère automatiquement :

- **summary.txt** : synthèse des problèmes détectés.
- **remediation_plan.csv** : plan de remédiation.
- **backlog.csv** : backlog priorisé.
- **roadmap.csv** : feuille de route de traitement.

---

## Exécution

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer le projet :

```bash
python app.py
```

Les résultats seront générés dans le dossier **output/**.

---

## Évolutions possibles

Cette première implémentation repose sur des règles de classification.

Une amélioration consisterait à intégrer un modèle de langage (LLM) afin de :

- générer automatiquement les actions correctives ;
- améliorer l'estimation de charge ;
- produire une priorisation plus contextuelle ;
- enrichir les recommandations techniques.

---

## Auteur

Projet réalisé dans le cadre d'un exercice de sélection portant sur l'utilisation de l'intelligence artificielle pour la génération d'un plan de remédiation.