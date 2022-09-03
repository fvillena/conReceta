from medications.models import CommercialProduct, ClinicalMedication
import csv


def run():
    with open('data/commercial_product.csv', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=';')

        CommercialProduct.objects.all().delete()

        for row in reader:
            name = row["Término Preferido"]
            concept_id = row["ConceptID"]
            state = row["Estado"]
            if state.strip() != "Vigente":
                continue
            clinical_medication_id, _, _ = row["ConceptID Fármacos - Medicamento Clínico ¦ Preferido Fármacos - Medicamento Clínico ¦ Estado"].split(
                "¦")
            clinical_medication_id = int(clinical_medication_id.strip())
            medication = CommercialProduct(
                concept_id=int(concept_id.strip()),
                name=name.strip(),
                clinical_medication = ClinicalMedication.objects.get(pk=clinical_medication_id)
            )
            medication.save()
