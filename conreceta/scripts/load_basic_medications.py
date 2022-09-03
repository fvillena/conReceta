from medications.models import BasicMedication
import csv


def run():
    with open('data/basic_medication.csv', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=';')

        BasicMedication.objects.all().delete()

        for row in reader:
            name = row["Término Preferido"]
            concept_id = row["ConceptID"]
            state = row["Estado"]
            if state.strip() != "Vigente":
                continue
            medication = BasicMedication(
                concept_id=int(concept_id.strip()),
                name=name.strip())
            medication.save()
