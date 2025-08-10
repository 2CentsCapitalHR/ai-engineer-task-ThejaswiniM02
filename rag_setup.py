import os
import requests
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.document import Document
from bs4 import BeautifulSoup

def clean_html(raw_html):
    """Remove HTML tags and extra whitespace."""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ No Gemini API key found. Please set GEMINI_API_KEY in your .env file.")

# ADGM official reference links (from Data Sources.pdf)
adgm_links = [
    "https://www.adgm.com/registration-authority/registration-and-incorporation",
    "https://www.adgm.com/setting-up",
    "https://www.adgm.com/legal-framework/guidance-and-policy-statements",
]

def fetch_and_split_docs():
    docs = []
    for url in adgm_links:
        try:
            print(f"📥 Fetching: {url}")
            text = requests.get(url, timeout=15).text
            clean_content = clean_html(text)
            docs.append(Document(page_content=clean_content, metadata={"source": url}))
        except Exception as e:
            print(f"⚠️ Failed to fetch {url}: {e}")
    # Split into chunks for embedding
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)

def build_vector_store():
    docs = fetch_and_split_docs()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("adgm_vectorstore")
    print("✅ RAG vector store built and saved locally in 'adgm_vectorstore/'")

if __name__ == "__main__":
    build_vector_store()
