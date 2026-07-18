import requests, json

user = "<soflane10>"  # mets ton pseudo GitHub ici
url = f"https://api.github.com/users/{user}/repos"

r = requests.get(url)
data = r.json()

if r.status_code == 200:
    # Afficher les noms et descriptions
    for repo in data:
        print(repo["name"], "-", repo["description"])

    # Sauvegarder dans un fichier JSON
    with open("repos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("✅ Dépôts sauvegardés dans repos.json")
else:
    print("Erreur:", r.status_code, data)
