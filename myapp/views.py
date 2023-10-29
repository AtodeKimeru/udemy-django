from django.shortcuts import render, HttpResponse, redirect


def index(request):
    years = range(2023, 2051)
    
    nombre = 'Iván Camilo'

    return render(request, 'index.html', {
        'title': 'Inicio',
        'years': years,
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
    })


def page(request, redir=0):

    if redir == 1:
        return redirect('contact', name="Atode", lastname="Kimeru")

    return render(request, 'page.html')


def contact(request, name="", lastname=""):
    return HttpResponse(f"<h2>This is contact page</h2><p>{name} {lastname}</p>")