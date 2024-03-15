# Guide d'installation du projet 

## Prérequis

- Python 3.8 ou supérieur
- [Poetry](https://python-poetry.org/) pour la gestion des dépendances

## Configuration de l'environnement

1. **Cloner le projet**

   Utilisez Git pour cloner le dépôt du projet dans votre environnement local.

   ```bash
   git clone https://github.com/Farid841/contact_app.git
   cd django_contact_app
   ```

2. **Configurer Poetry et l'environnement virtuel**

   Installez Poetry si ce n'est pas déjà fait, puis configurez l'environnement virtuel du projet.

   ```bash
   poetry install
   ```

   Cette commande installera toutes les dépendances nécessaires du projet dans un nouvel environnement virtuel.

3. **Activer l'environnement virtuel**

   Activez l'environnement virtuel géré par Poetry.

   ```bash
   poetry shell
   ```

## Configuration de la base de données

Par défaut, Django utilise SQLite comme système de base de données, ce qui est suffisant pour les projets de développement et de test.

1. **Effectuer les migrations**

   Créez les tables de base de données nécessaires en exécutant les migrations Django.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Lancer le serveur de développement

1. **Démarrer le serveur**

   Lancez le serveur de développement Django en utilisant la commande suivante :

   ```bash
   python manage.py runserver
   ```

2. **Accéder à l'application**

   Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/` pour voir l'application en action. 


# Prise d'une application déjà existante
Nous avons choisi de creer et utiliser l'application  appelée  pour avoir une liste de contact.
![Capture d'écran de l'application](image/home%20contact%20list.png)

## Bug Bash
J'ai réalisé un bug bash sur l'application en testant différentes fonctionnalités et en cherchant des anomalies ou des erreurs. J'ai identifié, c'est que le message ecrit dans le formualire ne s'affiche pas dans la liste de contact

## Diagramme de séquence
J'ai créé un diagramme de séquence pour représenter l'interaction entre les différents acteurs et les composants de l'application lors d'un scénario spécifique. Ce diagramme permet de visualiser le flux des actions et des messages échangés.  

#### Ajout d'un Contact
![Diagramme de sequence 1](image/diagramme%20de%20sequence%20contact)  
<u>Diagramme de sequence n°1</u>

#### Affichage des Contacts
![Diagramme de sequence 2](image/diagramme%20de%20sequence%202)
<u>Diagramme de sequence n°2</u>


## Diagramme d'activité
J'ai également réalisé un diagramme d'activité pour modéliser le déroulement des différentes activités et processus de l'application.

#### Soumission d'un Contact

![Soumission d'un Contact](image/diagramme%20d'activité%201)

#### Consultation des Contacts

![Consultation des Contacts](image/diagramme%20d'activité%202)

### Scénario de Test Vertical

Un scénario de test vertical a été conçu pour valider le processus complet de soumission d'un contact, de la saisie dans le formulaire à l'enregistrement dans la base de données et l'affichage dans la liste des contacts.

ajouter les chemas////

### Scénario de Test Horizontal

Un scénario de test horizontal a été mis en place pour tester l'interface utilisateur, en se concentrant sur la validation des champs du formulaire de contact et les messages d'erreur.

ajouter les chemas////

## Création d'une Branche de Staging

Une branche de staging a été créée pour effectuer les tests dans un environnement proche de la production (avant prod), permettant une isolation des tests et des développements en cours.

```bash
git checkout -b staging
