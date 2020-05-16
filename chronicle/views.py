from app.models import Journal
from django.shortcuts import render, get_object_or_404


def index(request):
    journals = Journal.objects.all()
    return render(request, 'home.html')
