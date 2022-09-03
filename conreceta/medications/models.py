from django.db import models

class ClinicalMedication(models.Model):
    concept_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    selling_condition = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%i/" % self.concept_id