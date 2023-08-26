from django.shortcuts import render, redirect
from .forms import PKPrzyjeciaForm
from .models import PK_Przyjecia

def dodaj_przyjecia(request):
    if request.method == 'POST':
        form = PKPrzyjeciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('strona_glowna')  # Zmień 'strona_glowna' na odpowiednią nazwę URL
    else:
        form = PKPrzyjeciaForm()
    return render(request, 'form_template.html', {'form': form})

def index(request):
    return render(request, 'index.html')

