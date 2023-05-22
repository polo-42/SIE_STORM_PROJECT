# SIE_STORM_PROJECT

Ce dossier contient :
- les fichiers de configuration pour notre projet de BI effectué sur Storm (STORM_CONFIGURATION)
- les fichiers csv et scripts python utilisés pour créer notre base de données (DATA_MANAGEMENT)

## DATA_MANAGEMENT
Pour rendre notre dataset utilisable par storm, nous avons du :
- formater les chiffres de la table games (transformer 30K en 30000, etc.)
- formater les dates de la tables games (transformer Dec 10, 2019 en 2019 (year), 10 (day) et 12 (month))
- formater les genres de la table genres (transformer ['Adventure', 'RPG'] en 'Adventure' et 'RPG')
- joindre les tables sales avec games (mapper les noms des jeux entre eux et stocker l'id du jeu dans sales)

*Ces différentes tâches ont été faites soit en excel soit en python*

Ensuite, les fichiers csv ont été transformé en sql et importé dans la base de données distante.

## STORM_CONFIGURATION
Il s'agit de la configuration de notre projet storm.

**Attention : LA CONNEXION A LA BASE DE DONNEES NECESSITE D'AJOUTER VOTRE IP DANS LES IPs DE CONFIANCE DE NOTRE SERVEUR**, veuillez nous contacter.

En important cette configuration, vous pouvez essayer le projet et ces dashboards. 

Afin de pouvoir visualiser notre projet sur Storm : 
1. Cliquez sur "ouvrir projet" sur Storm. 
2. Puis ouvrez le fichier SIE_STORM_PROJECT > STORM_CONFIGURATION > project.xml
3. Vous pouvez ensuite vous connecter avec l'utilisateur "storm" (sans mot de passe).
4. Explorer notre projet.