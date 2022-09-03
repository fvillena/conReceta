from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import ClinicalMedication

import random

def index(request):
    items = list(ClinicalMedication.objects.all())
    random_items = random.sample(items, 5)
    return render(request, 'medications/index.html', {'medications': random_items})
def detail(request, concept_id):
    try:
        medications = list(ClinicalMedication.objects.all())
        random_medications = random.sample(medications, 5)
        medication = ClinicalMedication.objects.get(pk=concept_id)
    except ClinicalMedication.DoesNotExist:
        raise Http404("Medication does not exist")
    return render(request, 'medications/detail.html', {'medication': medication, 'random_medications':random_medications})
def search_results(request):
    q = request.GET.get('q', '')
    results = ClinicalMedication.objects.filter(name__icontains=q.strip())[:100]
    return render(request, 'medications/search_results.html', {'results': results,'q':q})