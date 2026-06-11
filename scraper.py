import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Liste des URLs cibles de Safar Flyer
urls = [
    "https://www.royalairmaroc.com/fr-fr/safar-flyer/termes-et-conditions",
    "https://www.royalairmaroc.com/fr-fr/safar-flyer/nos-offres",
    "https://www.royalairmaroc.com/fr-fr/cash-miles",
    "https://www.royalairmaroc.com/fr-fr/safar-flyer/gagnez-des-miles"
    "https://www.royalairmaroc.com/ga-fr/safar-flyer/comment-ca-marche"
    "https://www.royalairmaroc.com/ga-fr/calculateur-de-miles"
    "https://www.royalairmaroc.com/fr-fr/safar-flyer/safar-family"
]

def extraire_texte_safar(urls_list):
    with open("safar_docs.txt", "w", encoding="utf-8") as f:
        for url in urls_list:
            print(f"Extraction de : {url}...")
            try:
                # 1. Télécharger la page
                response = requests.get(url, timeout=10)
                response.raise_for_status() # Vérifie si la page s'est bien chargée
                
                # 2. Analyser le HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 3. Nettoyage : On cible souvent la balise <main> ou les <div> de contenu
                # pour éviter de récupérer le menu de navigation ou le pied de page.
                content = soup.find('main') or soup.find('body')
                
                if content:
                    # Extraire le texte et supprimer les espaces inutiles
                    texte_propre = content.get_text(separator='\n', strip=True)
                    
                    # 4. Écrire dans le fichier
                    f.write(f"--- SOURCE: {url} ---\n")
                    f.write(texte_propre)
                    f.write("\n\n" + "="*50 + "\n\n")
                    
            except Exception as e:
                print(f"Erreur sur {url}: {e}")

    print("\nTerminé ! Le fichier 'safar_docs.txt' a été créé.")

if __name__ == "__main__":
    extraire_texte_safar(urls)
