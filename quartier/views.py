from django.shortcuts import render

def accueil(request):
    return render(request, 'quartier/accueil.html')
def apropos(request):
    return render(request, 'quartier/apropos.html')
def destinations(request):
    return render(request, 'quartier/destinations.html')
def culture(request):
    return render(request, 'quartier/culture.html')
def nature(request):
    return render(request, 'quartier/nature.html')
def contact(request):
    return render(request, 'quartier/contact.html')