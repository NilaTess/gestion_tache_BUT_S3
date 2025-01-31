# Project - Dev Efficace - S3

## Dévelopeur.euse.s
CHANDON Basile G1S3B p2304273
GIRAUD Nila G1S3A p2305739

## But du projet
Développer une application de **gestion de tâches**. L'utilisateur a la possibilité d'ajouter de nouvelles tâches selon ses besoins, de les catégoriser, de les rechercher et de suivre leur progression en les marquant comme terminées lorsqu'elles sont accomplies. 

### Manuel d'utilisation

Un visuel sur terminal à été effectué pour utiliser l'application.

#### Installation 

```git
git clone https://forge.univ-lyon1.fr/p2305739/project-dev-efficace-s3.git
```
Lancer l'application depuis le fichier **main.py** à la base du projet.

#### Utilisation

Lancer l'application depuis le terminal, un menu permet d'enclencher les différentes fonctionnalités.

##### **Base de Données**

Le fichier **"fichierDeBase.json"** dans le dossier **"./data/json"** contient les données importées de base dans l'application. 

##### **Type de données**

```python
    {
        "titre" : "", # String entre 1 et 50 caractrère.s
        "description" : "", # String entre 1 et 300 caractrère.s
        "responsable" : "", # String entre 1 et 25 caractère.s
        "priorite" : 0, # int  entre 1 et 10 
        "date_limite" : "" # String du type AAAA-MM-JJ
    },
```

##### **Import suplémentaire**

Il est possible d'importer d'autres fichiers Json en les ajoutant au dossier **"./json"** et en utilisant la fonctionnalité dans le terminal depuis le menu **"Données"**.

*Attention* : Il est nécessaire de donner le nom du fichier exact pour que l'importation s'effectue correctement.

#### Fonctionnalités principales

|Affichage          |Modification|Données   | 
|         -         |     -      |     -    |
|Afficher tâches    | Ajouter    | Importer |
|Tri                | Supprimer  |          |
|Recherche          | Modifier   |          |
|Afficher l'archive | Archiver   |          |
|                   |Désarchiver |          |

Le visuel du terminal reprend les grands titres du tableau comme base pour le menu.

### Technologies utilisés
##### Python 
Libraires | random, sys, os, time

            