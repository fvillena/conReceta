from medications.models import ClinicalMedication, BasicMedication
import csv


def run():
    with open('data/clinical_medication.csv', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=';')

        ClinicalMedication.objects.all().delete()

        for row in reader:
            name = row["Término Preferido"]
            concept_id = row["ConceptID"]
            state = row["Estado"]
            if state.strip() != "Vigente":
                continue
            basic_medication_id, _, _ = row["ConceptID Fármacos - Medicamento Básico ¦ Preferido Fármacos - Medicamento Básico ¦ Estado"].split("¦")
            medication = ClinicalMedication(
                concept_id=int(concept_id.strip()),
                name=name.strip(),
                selling_condition=row["Condición de Venta"].split("¦")[1].strip(),
                basic_medication = BasicMedication.objects.get(pk=basic_medication_id)
                )
            medication.save()
