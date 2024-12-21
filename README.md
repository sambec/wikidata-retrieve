

# Flask Wikidata Retrieval App

## Description

Cette application Flask permet de récupérer et d’afficher des informations sur une entité donnée à partir de l’API Wikidata. En utilisant un identifiant Wikidata, l’application interroge l’API et retourne une page HTML contenant :

- Les métadonnées de la réponse (code HTTP, type de contenu, etc.).
- Les données JSON de l'entité si elles sont disponibles.
- Un message d'erreur si l'identifiant est invalide ou si une erreur se produit.

---

## Fonctionnalités

1. **Route principale :**
   - `/retrieve_wikidata/<id>` : Accepte un identifiant Wikidata en tant que paramètre et affiche les informations correspondantes.
   
2. **Affichage dynamique :**
   - Utilise Jinja pour rendre une page HTML avec les données obtenues.

3. **Gestion des erreurs :**
   - Affiche des messages d'erreur clairs pour les identifiants invalides ou les erreurs réseau.

---

## Prérequis

Avant de commencer, assurez-vous d’avoir installé les outils suivants :

- **Python 3.10+**
- **Pip** (gestionnaire de packages pour Python)

---

## Installation

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/<votre_nom_utilisateur>/<nom_du_depot>.git
   cd <nom_du_depot>
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## Lancer l'application

1. Exécutez l’application Flask :
   ```bash
   python run.py
   ```

2. Accédez à l’application dans votre navigateur à l'adresse :
   ```
   http://127.0.0.1:5000/retrieve_wikidata/<id>
   ```
   Remplacez `<id>` par un identifiant Wikidata, par exemple `Q42` (Douglas Adams).

---

## Exemple

Pour l’identifiant `Q42`, l’application retournera une page HTML affichant :

- Le code HTTP : `200`
- Le type de contenu : `application/json`
- Les données JSON de l'entité : les informations de Douglas Adams.

En cas d’erreur (par exemple, un identifiant invalide), un message tel que : 
`"Aucune donnée trouvée pour cet identifiant."` sera affiché.

---

## Arborescence du projet

```plaintext
wikidata-retrieve/
│
├── app/                     # Dossier principal contenant l'application Flask
│   ├── app.py               # Fichier principal de l'application Flask
│   ├── config.py            # Fichier de configuration pour l'application
│   └── templates/           # Dossier contenant les fichiers HTML
│       └── wikidata.html    # Template Jinja pour afficher les résultats
├── requirements.txt         # Liste des dépendances Python
├── run.py                   # Fichier principal pour lancer l'application
└── README.md                # Documentation du projet
```

---

## Points d'amélioration

- Ajouter des tests unitaires pour vérifier la validité des réponses API.
- Intégrer une meilleure gestion des erreurs pour les exceptions inattendues.
- Améliorer le rendu HTML avec du CSS ou un framework comme Bootstrap.

---

## Ressources

- [Documentation Flask](https://flask.palletsprojects.com/)
- [API Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access)
- [Documentation Requests](https://docs.python-requests.org/)

---

## Crédits

Sarah Ambec avec l'aide de ChatGPT4 pour le cours de Python Flask de Maxime Challon en M2 Archives TNAH de l'Ecole des Chartes
