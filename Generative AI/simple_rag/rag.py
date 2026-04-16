
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

PDF_PATH = "LLM Cheatsheet.pdf"

# 1) Load PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

# 2) Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
splits = splitter.split_documents(docs)

# 3) Create embeddings + vector DB
emb = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-mpnet-base-v2",
    task="feature-extraction",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

vs = FAISS.from_documents(splits, emb)
retriever = vs.as_retriever(search_kwargs={"k": 4})

# 4) LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 5) Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer ONLY from the provided context. If not found, say you don't know."),
    ("human", "Question: {question}\n\nContext:\n{context}")
])

# Helper function
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

# 6) Ask questions (simple flow)
print("PDF RAG ready. Ask a question (Ctrl+C to exit).")

while True:
    q = input("\nQ: ").strip()

    # Step 1: Retrieve
    retrieved_docs = retriever.invoke(q)

    # Step 2: Format context
    context = format_docs(retrieved_docs)

    # Step 3: Create prompt
    final_prompt = prompt.invoke({
        "question": q,
        "context": context
    })

    # Step 4: Call LLM
    response = llm.invoke(final_prompt)

    # Step 5: Print
    print("\nA:", response.content)