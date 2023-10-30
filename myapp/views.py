from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from myapp.models import Article
from myapp.forms import FormArticle


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
        create_at = timezone.now(),
        update_at = timezone.now(),
    )
    articulo.save()
    return HttpResponse(f"Usuario creado: <strong>{articulo.title}</strong> - {articulo.content}")


def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']

        if len(title) <= 5:
            return HttpResponse("<h2>El titulo es muy pequeño</h2>")

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public,
            create_at = timezone.now(),
            update_at = timezone.now(),
        )
        articulo.save()

        return HttpResponse(f"Usuario creado: <strong>{articulo.title}</strong> - {articulo.content}")
    
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):

    return render(request, 'create_article.html')


def create_full_article(request):

    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():

            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
            title = title,
            content = content,
            public = public,
            create_at = timezone.now(),
            update_at = timezone.now(),
            )
            articulo.save()

            # Crear mensaje flash (sesión que solo se muestra una vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articles')

    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario,
    })


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
    articulo.update_at = timezone.now()

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")


def articulos(request):

    articulos_filtrados1 = Article.objects.filter(title__iexact="articulo")
    articulos_filtrados2 = Article.objects.filter(id__gte=9).exclude(public=False)
    articulos_filtrados = articulos_filtrados1 | articulos_filtrados2

    articulos_filtrados = Article.objects.raw("SELECT * FROM myapp_article WHERE title='articulo' AND public=1")

    articulos = Article.objects.filter(
        Q(id__contains="1") | Q(title__contains="artic")
    )
    articulos = Article.objects.all().order_by('-id')

    return render(request, 'articulos.html', {
        'articulos': articulos,
        'articulos_filtrados': articulos_filtrados,
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articles')
