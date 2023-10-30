from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Article


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

    return render(request, 'page.html',{
        'texto': "Xd",
        'lista': ['uno', 'dos', 'tres', 'cuatro', 'cinco'],
    })


def contact(request, name="", lastname=""):
    return HttpResponse(f"<h2>This is contact page</h2><p>{name} {lastname}</p>")


def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    return HttpResponse(f"Usuario creado: <strong>{articulo.title}</strong> - {articulo.content}")


def articulo(request):
    try:
        articulo = Article.objects.get(id=1, public=True)
        response = f"Articulo: <br> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Batman es el mejor superheroe"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")


def articulos(request):
    articulos = Article.objects.order_by('-id')[1:4]
    return render(request, 'articulos.html', {
        'articulos': articulos,
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articles')
