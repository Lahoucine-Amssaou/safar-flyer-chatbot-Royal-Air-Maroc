# Safar Flyer Chatbot

Chatbot RAG (Retrieval-Augmented Generation) basé sur les pages officielles
du programme de fidélité Safar Flyer de Royal Air Maroc.

Utilise **LangChain**, **Gemini 1.5 Flash** et **ChromaDB**.

## Architecture

1. `scraper.py` — extrait le contenu des pages Safar Flyer
2. `chatbot.py` — charge les documents, crée les embeddings, répond aux questions

## Installation

```bash
git clone https://github.com/ton-user/safar-flyer-chatbot
cd safar-flyer-chatbot
pip install -r requirements.txt
cp .env.example .env
# Remplis ta clé dans .env
```

## Utilisation

```bash
# Étape 1 : Scraper les données
python scraper.py

# Étape 2 : Lancer le chatbot
python chatbot.py
```

## Configuration

Crée un fichier `.env` à partir de `.env.example` et renseigne :
- `GOOGLE_API_KEY` : clé obtenue sur [Google AI Studio](https://aistudio.google.com/)

## Stack

- LangChain · ChromaDB · Gemini 1.5 Flash · BeautifulSoup4

## Note

Projet initialement développé en décembre 2025 dans le cadre d'un projet innovation à l'École Centrale Casablanca, en partenariat avec Royal Air Maroc.
