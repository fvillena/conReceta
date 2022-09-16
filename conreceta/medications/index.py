from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import CommercialProduct


@register(CommercialProduct)
class CommercialProductIndex(AlgoliaIndex):
    fields = ('concept_id', 'name', 'clinical_medication_name', 'basic_medication_name')
    index_name = 'conreceta'