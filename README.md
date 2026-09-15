# 📊 Analyse et Business Intelligence des données Jira

## 📌 Présentation du projet

Ce projet est réalisé dans le cadre d'un **stage de deux mois au sein de ISICOD – Ingénierie des Systèmes Informatiques**.

L'objectif du projet est de mettre en place une solution de **Business Intelligence (BI)** permettant d'exploiter les données issues de **Jira** afin de faciliter le suivi et l'analyse de la performance des projets.

La solution vise notamment à fournir une vision globale de l'évolution des projets, des tickets, des sprints et de l'activité des équipes.

---

## 🎯 Objectifs

Le projet a pour principaux objectifs de :

* comprendre la structure et le fonctionnement des données Jira ;
* identifier les données nécessaires à l'analyse des projets ;
* générer une base de données fictive inspirée de Jira ;
* préparer et contrôler la qualité des données ;
* nettoyer et transformer les données ;
* construire un modèle de données adapté à l'analyse ;
* développer des indicateurs clés de performance (KPI) ;
* créer des tableaux de bord interactifs avec **Power BI** ;
* analyser l'évolution et la performance des projets ;
* préparer, à terme, des fonctionnalités de prédiction de la performance des projets.

---

## 🏢 Contexte

Les données Jira contiennent différentes informations permettant de suivre l'activité des projets :

* projets ;
* tickets / issues ;
* utilisateurs ;
* types de tickets ;
* statuts ;
* priorités ;
* sprints ;
* historique des statuts ;
* commentaires ;
* temps de travail ;
* composants ;
* labels.

L'exploitation de ces données permet de construire une vision plus globale de l'activité des projets et d'aider les responsables à prendre des décisions basées sur les données.

---

## 🛠️ Technologies utilisées

### Programmation et génération des données

* **Python**
* **Faker**
* **Pandas**

### Business Intelligence

* **Power BI**
* **Power Query**
* **DAX**

### Gestion du code

* **Git**
* **GitHub**
* **Visual Studio Code**

---

## 📂 Structure du projet

```text
jira-project/
│
├── data/
│   ├── projects.csv
│   ├── users.csv
│   ├── issues.csv
│   ├── sprints.csv
│   ├── status_history.csv
│   ├── comments.csv
│   └── worklogs.csv
│
├── src/
│   └── generate_jira_data.py
│
├── notebooks/
│
├── powerbi/
│
├── docs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

> La structure peut évoluer au fur et à mesure de l'avancement du projet.

---

## 🔄 Étapes du projet

### 1. Étude de Jira

La première étape consiste à comprendre la structure des données Jira et les principales entités utilisées dans la gestion des projets.

Cette étude porte notamment sur :

* les projets ;
* les tickets ;
* les types de tickets ;
* les statuts ;
* les priorités ;
* les sprints ;
* les utilisateurs ;
* l'historique des tickets.

### 2. Génération d'une base de données fictive

Afin de disposer d'un environnement de travail sans dépendre immédiatement de données Jira réelles, une base de données fictive a été générée avec **Python et Faker**.

Cette base contient plusieurs fichiers CSV représentant différentes entités Jira.

### 3. Préparation et qualité des données

Cette étape prévue consiste à :

* vérifier la qualité des données ;
* identifier les valeurs manquantes ;
* détecter les incohérences ;
* supprimer les doublons ;
* transformer les données si nécessaire.

### 4. Modélisation des données

Les différentes sources de données seront organisées afin de construire un modèle adapté à l'analyse dans Power BI.

### 5. Création des KPI et tableaux de bord

Les données préparées seront ensuite utilisées pour créer des indicateurs permettant notamment d'analyser :

* le nombre de projets ;
* le nombre de tickets ;
* la répartition des tickets par statut ;
* la répartition par priorité ;
* l'avancement des projets ;
* la performance des sprints ;
* les tickets terminés et en cours ;
* les délais de traitement ;
* la charge de travail.

### 6. Analyse et prédiction

À terme, le projet pourra évoluer vers l'utilisation de techniques d'analyse prédictive afin d'identifier des tendances et d'aider à anticiper certains problèmes liés à la performance des projets.

---

## 📈 Résultat attendu

Le résultat final attendu est une solution de **Business Intelligence basée sur les données Jira**, permettant aux responsables de projets d'obtenir une vision claire de l'évolution de leurs projets grâce à des **KPI et des tableaux de bord interactifs**.

La solution doit faciliter :

* le suivi de l'avancement ;
* l'analyse de la charge de travail ;
* l'identification des problèmes ;
* le suivi des performances ;
* la prise de décision basée sur les données.

---

## ⚠️ Données

Les données actuellement utilisées dans le cadre du développement sont **fictives et synthétiques**.

Elles ont été générées afin de reproduire une structure similaire à celle de données Jira, sans utiliser de données réelles ou confidentielles de l'entreprise.

---

## 👩‍💻 Réalisation

**Dalal Machehoul**
Master Informatique – Gouvernance et Transformation Digitale
Université Mohammed V de Rabat

**Entreprise d'accueil :**
ISICOD – Ingénierie des Systèmes Informatiques

**Période :** Septembre – Octobre 2026

---

## 🚀 État actuel du projet

| Étape                              | État           |
| ---------------------------------- | -------------- |
| Étude de Jira                      | ✅ Réalisée     |
| Identification des données         | ✅ Réalisée     |
| Génération de la base fictive      | ✅ Réalisée     |
| Contrôle de la qualité des données | 🔄 À réaliser  |
| Nettoyage et transformation        | 🔄 À réaliser  |
| Modélisation                       | 🔄 À réaliser  |
| KPI                                | 🔄 À réaliser  |
| Dashboard Power BI                 | 🔄 À réaliser  |
| Analyse prédictive                 | 🔄 Perspective |

---

## 📌 Perspectives

Les prochaines évolutions du projet porteront principalement sur la préparation des données, la construction du modèle décisionnel et le développement des tableaux de bord Power BI.

À terme, l'objectif est de pouvoir exploiter des **données Jira réelles**, lorsque celles-ci seront disponibles et accessibles, afin de construire une solution adaptée au contexte de l'entreprise.
