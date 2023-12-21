from django.shortcuts import render
from .models import Moviedetails
# Create your views here.

def display(request):
    if request.method == 'POST':
        emoviename = request.POST['moviename']
        ebudjet = request.POST['budjet']
        edirector = request.POST['director']
        ehero = request.POST['hero']
        eheroine = request.POST['heroine']
        md = Moviedetails(moviename=emoviename,budjet=ebudjet,director=edirector,hero=ehero,heroine=eheroine)
        md.save()
    moviedetails = Moviedetails.objects.all()    
    return render(request,'index.html',{"data":moviedetails})