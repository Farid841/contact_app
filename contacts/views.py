from django.shortcuts import render, redirect

# Create your views here.
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()  # Récupère tous les contacts de la base de données
    if request.method == "POST":
        form = ContactForm(request.POST)  # Crée une instance de formulaire avec les données POST
        if form.is_valid():  # Vérifie la validité des données du formulaire
            form.save()  # Sauvegarde le nouveau contact dans la base de données
            return redirect('contact_list')  # Redirige l'utilisateur vers la liste des contacts après la soumission
    else:
        form = ContactForm()  # Crée une instance de formulaire vide pour une requête GET
    return render(request, 'contacts/contact_list.html', {'contacts': contacts, 'form': form})
