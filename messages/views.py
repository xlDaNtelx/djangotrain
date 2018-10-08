from django.http import HttpResponse
from django.shortcuts import render
from .forms import MessageForm
from .models import Message


def home_view(request, *args, **kwargs):
    obj = Message.objects.get(id=1)
    form = MessageForm(request.POST)
    # if form.is_valid():
    #     form.save()

    context = {
        'form': form
    }

    return render(request, "home.html", context)
