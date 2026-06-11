import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

load_dotenv()  # Charge la clé depuis le fichier .env


def creer_chatbot_safar():
    print("Initialisation du cerveau du chatbot...")
    
    # 1. CHARGEMENT DU FICHIER (celui généré avec le script scraper.py)
    if not os.path.exists("safar_docs.txt"):
        print("Erreur : Le fichier 'safar_docs.txt' est introuvable.")
        return None

    loader = TextLoader("safar_docs.txt", encoding="utf-8")
    documents = loader.load()

    # 2. DÉCOUPAGE DU TEXTE
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    # 3. CRÉATION DES EMBEDDINGS (Version Google)
    # On utilise un modèle gratuit pour transformer le texte en vecteurs
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Stockage en mémoire locale
    vectorstore = Chroma.from_documents(texts, embeddings)

    # 4. CONFIGURATION DU MODÈLE GEMINI (Version 1.5 Flash)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

    # 5. CRÉATION DU SYSTÈME DE RÉPONSE
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}) # Cherche les 3 meilleurs extraits
    )
    
    return qa_chain

# LANCEMENT DU CHATBOT
bot = creer_chatbot_safar()

if bot:
    print("\n--- Assistant Safar Flyer (Gemini) prêt ! ---")
    print("(Tapez 'quitter' pour arrêter)\n")
    
    while True:
        query = input("Client: ")
        if query.lower() in ['quitter', 'exit', 'stop']:
            break
        
        try:
            # L'IA va chercher dans 'safar_docs.txt' avant de répondre
            reponse = bot.invoke(query)
            print(f"\nIA: {reponse['result']}\n")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
