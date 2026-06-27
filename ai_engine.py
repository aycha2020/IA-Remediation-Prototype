import pandas as pd


# Classification de la criticité


CRITICAL_CATEGORIES = {
    "Security": "Critique",
    "Performance": "Élevée",
    "Testing": "Élevée",
    "Architecture": "Moyenne",
    "Database": "Moyenne",
    "Code Quality": "Faible",
    "Documentation": "Faible",
    "DevOps": "Moyenne"
}


# Priorité


PRIORITY = {
    "Critique": "P1",
    "Élevée": "P2",
    "Moyenne": "P3",
    "Faible": "P4"
}

# Estimation (jours/homme)


ESTIMATION = {
    "Critique": 5,
    "Élevée": 3,
    "Moyenne": 2,
    "Faible": 1
}


# Actions correctives


ACTIONS = {
    "Security": "Corriger la vulnérabilité et appliquer les bonnes pratiques de sécurité.",
    "Performance": "Optimiser les performances et réduire les temps de réponse.",
    "Code Quality": "Refactoriser le code et supprimer les duplications.",
    "Documentation": "Compléter la documentation technique.",
    "Testing": "Mettre en place des tests automatisés.",
    "Architecture": "Revoir l'architecture afin de réduire le couplage.",
    "Database": "Améliorer la qualité et l'intégrité des données.",
    "DevOps": "Automatiser le déploiement et renforcer la supervision."
}


def analyze_findings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyse les constats techniques et génère
    criticité, priorité, estimation et action corrective.
    """

    result = df.copy()

    result["Criticité"] = result["Category"].map(CRITICAL_CATEGORIES)
    result["Priorité"] = result["Criticité"].map(PRIORITY)
    result["Charge (jours)"] = result["Criticité"].map(ESTIMATION)
    result["Action corrective"] = result["Category"].map(ACTIONS)

    return result


def generate_summary(df: pd.DataFrame) -> str:

    total = len(df)

    critique = (df["Criticité"] == "Critique").sum()
    elevee = (df["Criticité"] == "Élevée").sum()
    moyenne = (df["Criticité"] == "Moyenne").sum()
    faible = (df["Criticité"] == "Faible").sum()

    txt = f"""

SYNTHÈSE DE L'AUDIT


Nombre total de constats : {total}

Critiques : {critique}

Élevés : {elevee}

Moyens : {moyenne}

Faibles : {faible}

Les éléments critiques doivent être traités en priorité,
suivis des problèmes de performance,
des sujets d'architecture,
puis des améliorations de qualité et de documentation.

"""

    return txt