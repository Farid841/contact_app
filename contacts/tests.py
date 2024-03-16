from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .forms import ContactForm

class ContactTests(TestCase):

    def test_create_contact(self):
        # URL de la vue qui gère la liste et la création des contacts
        url = reverse('contact_list')
        
        # Données du formulaire qui simulent une entrée utilisateur valide
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'message': 'Hello, this is John.'
        }
        
        # Envoi d'une requête POST avec les données du formulaire
        response = self.client.post(url, data)
        
        # Vérification que la requête a réussi et redirigé vers la même page
        self.assertEqual(response.status_code, 302)  # 302 est le code pour une redirection
        
        # Vérification que le contact a bien été créé dans la base de données
        self.assertEqual(Contact.objects.count(), 1)
        new_contact = Contact.objects.first()
        self.assertEqual(new_contact.name, 'John Doe')
        self.assertEqual(new_contact.email, 'john@example.com')
        self.assertEqual(new_contact.phone, '1234567890')
        self.assertEqual(new_contact.message, 'Hello, this is John.')

    def test_contact_list_includes_new_contact(self):
        # Création d'un contact de test dans la base de données
        Contact.objects.create(name='Jane Doe', email='jane@example.com', phone='0987654321', message='Hi there!')

        # Récupération de la page de la liste des contacts
        response = self.client.get(reverse('contact_list'))
        
        # Vérification que la page s'affiche correctement
        self.assertEqual(response.status_code, 200)
        
        # Vérification que le contenu de la page inclut le nom du contact ajouté
        self.assertContains(response, 'Jane Doe')
        self.assertContains(response, 'jane@example.com')
