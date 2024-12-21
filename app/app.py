from flask import Flask, request, render_template, jsonify
import requests
from .config import Config

app = Flask(__name__)

#une route pour la racine
@app.route("/")
def index():
    return "la route en fait c'est avec '/retrieve_wikidata/(id)'"

#la route pour faire vraiment tourner l'application
@app.route('/retrieve_wikidata/<id>')
def retrieve_wikidata(id):
    """
    Route Flask pour récupérer des informations depuis Wikidata.
    :param id: Identifiant Wikidata de l'entité à interroger.
    :return: Page HTML avec les résultats ou un message d'erreur.
    """
    # API de Wikidata
    wikidata_url = f"https://www.wikidata.org/wiki/Special:EntityData/{id}.json"
    
    try:
        # Envoi de la requête à l'API de Wikidata
        response = requests.get(wikidata_url)
        
        # Récupération des métadonnées
        http_status = response.status_code
        content_type = response.headers.get("Content-Type", "unknown")
        
        # print(f"HTTP {http_status} - TYPE {content_type}")

        if http_status == 200 and "application/json" in content_type:
            # Décodage des données JSON
            json_data = response.json()
            
            # print("HERE")

            # Vérification des données disponibles
            if id in json_data.get("entities", {}):
                entity_data = json_data["entities"][id]
            else:
                entity_data = None
        else:
            # En cas de réponse inattendue
            json_data = None
            entity_data = None

        # Préparation des données pour le rendu
        return render_template(
            "wikidata.html",
            status_code=http_status,
            content_type=content_type,
            entity_data=entity_data,
            error_message=None if entity_data else "Aucune donnée trouvée pour cet identifiant.",
        )
    
    except requests.RequestException as e:
        # Gestion des erreurs de connexion
        return render_template(
            "wikidata.html",
            status_code=None,
            content_type=None,
            entity_data=None,
            error_message=f"Erreur lors de la requête : {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
