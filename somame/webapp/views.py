from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import RegisterFormUp
from .models import RegisterForm


# Create your views here.
def Register(request):
    title = 'Subscribe to our Mailing list for Awesome Deals'

    form = RegisterFormUp(request.POST or None)

    context = {
        "title": title,
        "form" : form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)

        context = {
            "title": "Thank you for Subscribing! \n ",
        }
    return render(request, '../templates/form.html', context)
