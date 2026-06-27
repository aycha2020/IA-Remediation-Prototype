import os
import pandas as pd
from ai_engine import analyze_findings, generate_summary


# Création du dossier output

os.makedirs("output", exist_ok=True)

# Lecture du fichier audit

input_file = "data/audit.csv"

df = pd.read_csv(input_file)

print("Fichier chargé avec succès.")
print(f"Nombre de constats : {len(df)}")

# Analyse IA

result = analyze_findings(df)

# Génération du résumé

summary = generate_summary(result)

with open("output/summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

# Plan de remédiation

remediation = result[
    [
        "ID",
        "Category",
        "Finding",
        "Criticité",
        "Action corrective",
        "Charge (jours)",
        "Depends_On",
    ]
]

remediation.to_csv(
    "output/remediation_plan.csv",
    index=False,
    encoding="utf-8-sig",
)

# Backlog

backlog = result[
    [
        "ID",
        "Finding",
        "Priorité",
        "Charge (jours)",
        "Depends_On",
        "Status",
    ]
]

ordre = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}

backlog["Ordre"] = backlog["Priorité"].map(ordre)

backlog = backlog.sort_values("Ordre")

backlog = backlog.drop(columns=["Ordre"])

backlog.to_csv(
    "output/backlog.csv",
    index=False,
    encoding="utf-8-sig",
)

# Roadmap

roadmap = []

for p in ["P1", "P2", "P3", "P4"]:

    tasks = backlog[backlog["Priorité"] == p]

    roadmap.append(
        {
            "Sprint": p,
            "Nombre de tâches": len(tasks),
            "Charge totale": tasks["Charge (jours)"].sum(),
        }
    )

roadmap = pd.DataFrame(roadmap)

roadmap.to_csv(
    "output/roadmap.csv",
    index=False,
    encoding="utf-8-sig",
)

# Console

print("-------------------------------------")
print("Analyse terminée.")
print("Les fichiers ont été générés :")
print("✔ summary.txt")
print("✔ remediation_plan.csv")
print("✔ backlog.csv")
print("✔ roadmap.csv")
print("-------------------------------------")