"""NewBeginning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/<str:name>/<str:lastname>', views.contact, name='contact'),
    path('page/', views.page, name='page'),
    path('page/<int:redir>', views.page, name='page'),
    path('create-article/<str:title>/<str:content>/<str:public>', views.crear_articulo, name='create_article'),
    path('article/', views.articulo, name='article'),
    path('edit-article/<int:id>', views.editar_articulo, name='edit_article'),
    path('articles/', views.articulos, name='articles'),
    path('delete-article/<int:id>', views.borrar_articulo, name='delete'),
    path('save-article/', views.save_article, name='save'),
    path('create-article/', views.create_article, name='create'),
    path('create-full-article/', views.create_full_article, name='create_full'),
]

# configuración  para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)