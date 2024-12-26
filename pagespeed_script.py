import requests

def get_pagespeed_insights(url):
    """
    Fetch PageSpeed Insights data for a given URL using the Google PageSpeed Insights API.
    """
    api_key = "AIzaSyAgtu89igIuQ2pE6-ezOGyy6WmsRkVFNkc"  
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    params = {
        "url": url,
        "key": api_key,
        "strategy": "mobile",  # Options: "mobile" or "desktop"
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Erreur {response.status_code}: {response.text}"}

# Exemple d'utilisation
if __name__ == "__main__":
    test_url = input("Entrez l'URL du site à auditer : ")
    results = get_pagespeed_insights(test_url)

    if "error" in results:
        print(results["error"])
    else:
        lighthouse_result = results.get("lighthouseResult", {})
        performance_score = lighthouse_result.get("categories", {}).get("performance", {}).get("score", "N/A")

        print(f"Score de Performance : {performance_score * 100 if performance_score != 'N/A' else 'N/A'}")
