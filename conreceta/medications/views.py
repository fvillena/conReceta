from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import Q

from .models import CommercialProduct

import random

def index(request):
    items = list(CommercialProduct.objects.all())
    random_items = random.sample(items, 5)
    return render(request, 'medications/index.html', {'medications': random_items})
def detail(request, concept_id):
    try:
        medications = list(CommercialProduct.objects.all())
        random_medications = random.sample(medications, 5)
        medication = CommercialProduct.objects.get(pk=concept_id)
        siblings = medication.clinical_medication.commercialproduct_set.all()
    except CommercialProduct.DoesNotExist:
        raise Http404("Medication does not exist")
    return render(request, 'medications/detail.html', {'medication': medication, 'random_medications':random_medications, 'siblings':siblings})
def search_results(request):
    q = request.GET.get('q', '')
    results = CommercialProduct.objects.filter(
        Q(name__icontains=q.strip())
        | Q(clinical_medication__name__icontains=q.strip())
        )[:100]
    return render(request, 'medications/search_results.html', {'results': results,'q':q})