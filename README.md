Farid841: Prendre une application déjà existante
• Faire un bug bash
• Faire au moins un diagramme de séquence
• Faire au moins un diagramme d’activité
• Ecrire un Scénario de test vertical
• Ecrire un Scénario de test horizontal
• Créer une branche de staging
• Exécutez le bug bash et faites une remontée de
bug
• Bonus : intégrer un outil d’automatisation des
tests (unitaire, intégration ou e2e)

donne moi un bon template pour repondre a ses questions 
en te basant sur mon projets stp

GitHub Copilot: Voici un exemple de template pour répondre aux questions en se basant sur votre projet :

## Prise d'une application déjà existante
Nous avons choisi d'utiliser une application existante appelée "django_contact_app" pour avoir une liste de contact.
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
