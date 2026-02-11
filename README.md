TP : Formulaire d'Identification Sécurisé
Auteur: Vincent BERNIER

--Informations Techniques--

Prérequis
- python/python3
- SQLite3

Dépendances
- sqlite3
- bcrypt
- os
- re

Technologie
- Serveur backend : python
- Serveur client : javascript
- Interface Graphique : HTML et CSS
- Base de données : SQLite3

--Utilisation--

Execution
- python3 formulaire.py
- Ouvir sur un navigateur une page a l'adresse : http://localhost:5000/

Test
-Pour utiliser le formulaire, il est nécessaire de créer un profil au préalable avec le bouton créer un compte.
Un compte de test est pré a l'emploi est disponible :
  - utilisateur  : `test`
  - mot de passe : `test`

--Implémentation--
L'application affiche un formulaire d'identification avec les éléments suivantes :

Fenêtre Principale avec :
- Un premier champ pour un "Identifiant"
      - On autoriser :
            - lettres (a-z, A-Z)
            - chiffres (0-9)
            - underscore
            - entre 3 et 15 caractères

- Un second champ pour un "mot de passe"
- 3 boutons :
      - bouton "connexion" pour vérifier les informations
      - bouton "Créer un compte" ouvrir une fenêtre d'inscription
      - bouton "Reset" qui vide tous les champs du formulaire

Fenêtre d'inscription avec :
- Un premier champ pour un "Identifiant"
- Un second champ pour un "mot de passe"
- Un troisième champ pour la confirmation du mot de passe
- 2 boutons :
      - bouton "créer le compte" pour créer un profils identifiant/mot de passe une fois tout les champs correctement remplie
      - bouton "retour" pour fermer la fenêtre d'inscription 

Gestion de base de données avec SQLite
- Création d'un fichier data_user.db même répertoire que le code source
- Le fichier contient une table "users" avec les colonnes suivantes :
      - "id" : Identifiant unique
      - "username" : Identifiant choisie par l'utilisateur
      - "password_hash" : Mot de passe choisie par l'utilisateur haché en SHA-256

--Sécurité--
- Les mots de passe sont hachés avec bcrypt
- Les mots de passe ne s'affichent pas à l'écran
- Prévention des injections SQL avec les requêtes SQLite utilisent des paramètres (`?`) et des context managers (`with sqlite3.connect(...)`).
- Regex simple
