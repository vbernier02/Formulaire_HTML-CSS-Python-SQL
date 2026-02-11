# TP – Formulaire d’Identification Sécurisé

**Auteur : Vincent BERNIER**

---

## Description

Application web permettant la création et la connexion sécurisée d’utilisateurs via un formulaire d’identification.

Le projet met en œuvre :
- Un backend en **Python**
- Une base de données **SQLite3**
- Une interface client en **HTML, CSS et JavaScript**
- Un système de hachage sécurisé des mots de passe avec **bcrypt**

---

## Informations Techniques

### Prérequis

- Python 3
- SQLite3

### Dépendances Python

- `sqlite3`
- `Flask`
- `bcrypt`
- `os`
- `re`

Installation si nécessaire :

```bash
pip install bcrypt
```
```bash
pip install Flask
```

---

## Technologies Utilisées

| Composant        | Technologie |
|------------------|------------|
| Backend          | Python     |
| Client           | JavaScript |
| Interface        | HTML / CSS |
| Base de données  | SQLite3    |
| Framework        | Flask      |

---

## Utilisation

### Lancer l’application

```bash
python3 formulaire.py
```

Puis ouvrir dans un navigateur :

```
http://localhost:5000/
```

---

## Compte de Test

Un compte est déjà disponible :

- **Utilisateur** : `test`
- **Mot de passe** : `test`

---

## Fonctionnalités

### Fenêtre Principale

- Champ **Identifiant**
  - Autorise : lettres (a-z, A-Z), chiffres (0-9), underscore
  - Longueur : entre 3 et 15 caractères
- Champ **Mot de passe**
- Boutons :
  - `Connexion`
  - `Créer un compte`
  - `Reset` (vide les champs)

---

### Fenêtre d’Inscription

- Champ **Identifiant**
- Champ **Mot de passe**
- Champ **Confirmation du mot de passe**
- Boutons :
  - `Créer le compte`
  - `Retour`

---

## Gestion de la Base de Données

- Création automatique du fichier :  
  `data_user.db`
- Base SQLite contenant une table `users`

### Structure de la table `users`

| Colonne        | Description |
|---------------|-------------|
| id            | Identifiant unique |
| username      | Identifiant utilisateur |
| password_hash | Mot de passe haché |

---
## Sécurité

- Hachage des mots de passe avec **bcrypt**
- Les mots de passe ne s’affichent pas à l’écran
- Protection contre les injections SQL :
  - Requêtes paramétrées (`?`)
  - Utilisation de `with sqlite3.connect(...)`
  - Validation des identifiants via **Regex**
