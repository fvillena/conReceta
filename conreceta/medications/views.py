from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Medication

import random

def index(request):
    items = list(Medication.objects.all())
    random_items = random.sample(items, 5)
    return render(request, 'medications/index.html', {'medications': random_items})
def detail(request, concept_id):
    try:
        medications = list(Medication.objects.all())
        random_medications = random.sample(medications, 5)
        medication = Medication.objects.get(pk=concept_id)
    except Medication.DoesNotExist:
        raise Http404("Medication does not exist")
    return render(request, 'medications/detail.html', {'medication': medication, 'random_medications':random_medications})