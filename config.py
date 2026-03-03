from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.embeddings import Model2vecEmbeddings

# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# DATABASE_URL = "sqlite:///./chat.db"
DATABASE_URL = "postgresql+psycopg://esai:1234@localhost/dd"

engine = create_engine(
    DATABASE_URL,
    # echo=True,
    # connect_args={"check_same_thread": False},  # required for SQLite
)

DB_Session = sessionmaker(autoflush=True, bind=engine)

Base = declarative_base()


# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

embeddings = Model2vecEmbeddings("minishlab/potion-base-8M")
connection = "postgresql+psycopg2://esai:1234@localhost:5432/vector"

collection_name = "scam_tech_support"


vector_store = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)


llm = init_chat_model(
    model="openai:o4-mini",
    # model="llama-3.3-70b-versatile",
    # model_provider="openai",
    # model_provider="groq",
    # temperature=0.2,
    max_tokens=720,
)

print(llm)
