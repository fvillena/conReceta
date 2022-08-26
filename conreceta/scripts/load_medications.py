from medications.models import Medication
import csv


def run():
    with open('data/medications.csv', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=';')

        Medication.objects.all().delete()

        for row in reader:
            basic_medication_data = row["ConceptID Fármacos - Medicamento Básico ¦ Preferido Fármacos - Medicamento Básico ¦ Estado"]
            if len(basic_medication_data.split("¦")) != 3:
                continue
            concept_id, name, state = basic_medication_data.split("¦")
            if state.strip() != "Vigente":
                continue
            other_medication_data = row["Vía Administración ¦ Orden"]
            if len(other_medication_data.split("¦")) != 3:
                continue
            _, route, _ = other_medication_data.split("¦")
            if route.strip() != "oral":
                continue
            medication = Medication(
                concept_id=int(concept_id.strip()),
                name=name.strip(),
                selling_condition=row["Condición de Venta"].split("¦")[1].strip())
            medication.save()
