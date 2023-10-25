from django.shortcuts import render, HttpResponse, redirect


def index(request):
    years = "<ul>"
    n = 2023
    for i in range(10):
        n += i
        years += f"<li>{n}</li>"
    years += "</ul>"

    return render(request, 'index.html', {
        years: years,
    })


def page(request, redir=0):

    if redir == 1:
        return redirect('contact', name="Atode", lastname="Kimeru")

    return render(request, 'page.html')


def contact(request, name="", lastname=""):
    return HttpResponse(f"<h2>This is contact page</h2><p>{name} {lastname}</p>")