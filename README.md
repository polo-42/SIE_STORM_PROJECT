# SIE_STORM_PROJECT

Ce dossier contient :
- les fichiers de configuration pour notre projet de BI effectué sur Storm (STORM_CONFIGURATION)
- les fichiers csv et scripts python utilisés pour créer notre base de données (DATA_MANAGEMENT)

## Recréer le projet
1. Importer la bases de données mySQL depuis le fichier games.sql
2. Importer le projet storm : upload project + SIE_STORM_PROJECT > STORM_CONFIGURATION
3. Changer la config avec les informations de la bases de données que vous avez recréer au point 1 (changer user, password, host et dbs)
4. Explorer notre projet.

## DATA_MANAGEMENT
Pour rendre notre dataset utilisable par storm, nous avons du :
- formater les chiffres de la table games (transformer 30K en 30000, etc.)
- formater les dates de la tables games (transformer Dec 10, 2019 en 2019 (year), 10 (day) et 12 (month))
- formater les genres de la table genres (transformer ['Adventure', 'RPG'] en 'Adventure' et 'RPG')
- joindre les tables sales avec games (mapper les noms des jeux entre eux et stocker l'id du jeu dans sales)

*Ces différentes tâches ont été faites soit en excel soit en python*

Ensuite, les fichiers csv ont été transformé en sql et importé dans la base de données distante.

Le schéma du dataset dans Storm : 

<img src="./.img/schema.png" alt="Storm Schema" style="height:500px;" />

## STORM_CONFIGURATION
Il s'agit de la configuration de notre projet storm.

**Attention : LA CONNEXION A LA BASE DE DONNEES NECESSITE D'AJOUTER VOTRE IP DANS LES IPs DE CONFIANCE DE NOTRE SERVEUR**. 

Dans l'état, le projet ne pourra pas charger les données. Pour se faire voir la section : Recréer le projet.

En important cette configuration, vous pouvez essayer le projet et ces dashboards. 

### Screenshots des dashboards

#### Dashboard games avec une sélection des 50 meilleurs jeux et le wordcloud des genres liés aux jeux
<img src="./.img/games.png" alt="Dashboard Storm games" style="height:500px;" />

#### Page ratings des jeux
<img src="./.img/ratings.png" alt="Dashboard Storm games" style="height:500px;" />

#### Page reviews des jeux
<img src="./.img/reviews.png" alt="Dashboard Storm games" style="height:500px;" />

#### Dashboard genres représentant les genres les plus représentés pour nos jeux
<img src="./.img/genres.png" alt="Dashboard Storm games" style="height:500px;" />

#### Dashboard sales représentatn les ventes totales du secteur jeu vidéo selon les régions
<img src="./.img/sales.png" alt="Dashboard Storm games" style="height:500px;" />