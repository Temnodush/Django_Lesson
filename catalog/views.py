from django.shortcuts import render

def home(request):
    """Контроллер для главной страницы"""
    return render(request, 'home.html')

def contacts(request):
    """Контроллер для страницы контактов"""
    return render(request, 'contacts.html')