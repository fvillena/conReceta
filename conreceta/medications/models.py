from django.db import models

class BasicMedication(models.Model):
    concept_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ClinicalMedication(models.Model):
    concept_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    selling_condition = models.CharField(max_length=255)
    basic_medication = models.ForeignKey(BasicMedication, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CommercialProduct(models.Model):
    concept_id = models.PositiveIntegerField(primary_key=True)
    clinical_medication = models.ForeignKey(ClinicalMedication, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def clinical_medication_name(self):
        return self.clinical_medication.name
    
    def basic_medication_name(self):
        return self.clinical_medication.basic_medication.name

    def get_absolute_url(self):
        return "/%i/" % self.concept_id
    
    def __str__(self):
        return self.name