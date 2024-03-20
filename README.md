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

## REPONSE AU TP1

ici le tp en question: [Link to PDF File](image/Test%20Fonctionnels%20E2E%203.pdf).
| Tâche                                        | Statut |
|---------------------------------------------|:------:|
| Prendre une application déjà existante      | ✅     |
| Faire un bug bash                           |   ✅     |
| Faire au moins un diagramme de séquence     | ✅ |
| Faire au moins un diagramme d’activité      | ✅   |
| Ecrire un Scénario de test vertical         | ✅   |
| Ecrire un Scénario de test horizontal       | ✅|
| Créer une branche de staging                | ✅ |
| Exécutez le bug bash et faites une remontée de bug | ✅  |
| Bonus : intégrer un outil d’automatisation des tests (unitaire, intégration ou e2e) |  ✅ |

Nous avons choisi de creer et utiliser l'application  appelée  pour avoir une liste de contact.
![Capture d'écran de l'application](image/home%20contact%20list.png)

## Diagramme de séquence

J'ai créé un diagramme de séquence pour représenter l'interaction entre les différents acteurs et les composants de l'application lors d'un scénario spécifique. Ce diagramme permet de visualiser le flux des actions et des messages échangés.  

### Ajout d'un Contact

![Diagramme de sequence 1](image/diagramme%20de%20sequence%20contact)  
<u>Diagramme de sequence n°1</u>

### Affichage des Contacts

![Diagramme de sequence 2](image/diagramme%20de%20sequence%202)
<u>Diagramme de sequence n°2</u>

## Diagramme d'activité

J'ai également réalisé un diagramme d'activité pour modéliser le déroulement des différentes activités et processus de l'application.

### Soumission d'un Contact

![Soumission d'un Contact](image/diagramme%20d'activité%201)

### Consultation des Contacts

![Consultation des Contacts](image/diagramme%20d'activité%202)

### Scénario de Test Vertical

Un scénario de test vertical a été conçu pour valider le processus complet de soumission d'un contact, de la saisie dans le formulaire à l'enregistrement dans la base de données et l'affichage dans la liste des contacts.

1. Accéder au formulaire de contact.
2. Ajouter le nom du contact dans le champ prévu à cet effet.
3. Ajouter l'e-mail du contact dans le champ prévu à cet effet.
4. Ajouter le numéro de téléphone du contact dans le champ prévu à cet effet.
5. Ajouter un message ou une note pour le contact dans le champ prévu à cet effet (optionnel).
6. Cliquer sur le bouton de soumission du formulaire.
7. Vérifier l'affichage du message de succès après soumission du formulaire.
8. Vérifier que les données du nouveau contact sont correctement enregistrées et affichées dans la liste des contacts.

### Scénario de Test Horizontal

Un scénario de test horizontal a été mis en place pour tester l'interface utilisateur, en se concentrant sur la validation des champs du formulaire de contact et les messages d'erreur.

| Étape | Ajouter un message dans le champ prévu à cet effet. | Ajouter le nom du contact dans le champ prévu à cet effet. | Cliquer sur le bouton de soumission du formulaire. | Accéder au formulaire de contact. | Vérifier l'affichage du message de succès. | Ajouter le numéro de téléphone dans le champ prévu à cet effet. | Vérifier que les données du nouveau contact sont correctement enregistrées. | Ajouter l'e-mail du contact dans le champ prévu à cet effet. |
|-------|--------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------|---------------------------------------|-----------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|




-----------------------------------------
|-------|--------------------------------|----|-----|-----------------------------------------|------------|
| 1     |               | ✅  |     |                                         |       |
| 2     |              | ✅ |     | Le message "Champ requis" s'affiche      |            |
| 3     | Format 'Email' invalide        | ✅  |   |                                            |        |
| 4     | Champ 'Téléphone' vide         | ✅ |     | Le message "Champ requis" s'affiche      |            |
| 5     | Format 'Téléphone' invalide    |    | ✅  | Aucun message d'erreur pour le format    | #203       |
| 6     | Champ 'Message' vide           | ✅ |     | Le formulaire est soumis sans message    |            |
| 7     | Longueur 'Message' excessive   |    | ✅  | Le formulaire accepte un message trop long | #204     |
| 8     | Soumission du formulaire complet | ✅ |   |                                          |            |
| 9     | Réinitialisation du formulaire | ✅ |     | Les champs ne sont pas réinitialisés après soumission | |

## Création d'une Branche de Staging

Une branche de staging a été créée pour effectuer les tests dans un environnement proche de la production (avant prod), permettant une isolation des tests et des développements en cours.

```bash
git checkout -b staging
```

## Exécution du Bug Bash

Voici le tableau récapitulatif des bugs identifiés lors du Bug Bash :

| Bug           | Description                        | Ticket | Statut |
|---------------|------------------------------------|--------|--------|
| Numéro de tel invalide | Le numéro de téléphone accepte des caractères non autorisés | #2 | OK |
| Champ nom invalide | Le champ nom accepte des caractères spéciaux et numériques | #3 | OK |
| Nombre de caractères invalide du numéro de tel | Le numéro de téléphone ne respecte pas la longueur requise | #4 | OK |

### Suivi

- **Plan de Correction** :
 - Bug 1: Numéro de tel invalide
    - Solution: Accepter les caracteres `[0-9]` uniquement
 - Bug 2: Le champ nom invalide
    - Solution: Interdire les caracters `[0-9]` & speciaux sauf `-`
 - Bug 3: Nombre de caraterer invalide du numero de tel  
    - Solution: nombre de caracteres minimum & maximum = 10 (n°tel français)
 
## Intégration d'un Outil d'Automatisation des Tests

### Choix de l'Outil

- **Outil(s) Sélectionné(s)** : django test (tool chain de test django)

### Écriture des Tests

- **Tests Unitaires** :
  - Test 1: test de creation d'un nouveau contact
  - Test 2: test de verification d'un contact qu'on vient de creer

### Exécution et Maintenance des Tests

- **Exécution des Tests** :

```bash
python manage.py test
```

- **Capture d'écran** :
![resultat de test](image/resultat%20de%20test.png)

- **code** : [chemin vers le code de test](contacts/tests.py)
