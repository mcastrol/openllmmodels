#https://python.langchain.com/v0.2/docs/integrations/document_loaders/unstructured_file/
#https://python.langchain.com/v0.2/docs/integrations/document_loaders/unstructured_file/
import os
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient


api_key=os.getenv("OPENAI_API_KEY")
docs_dir="data/"
file_name="Databricks-Big-Book-Of-GenAI-FINAL.pdf"
qdrant_url="http://localhost:6333/"
embedding_model="text-embedding-ada-002"
qdrant_collection="databricks-big-book"
strategy="fast"

loader = UnstructuredFileLoader(f"{docs_dir}{file_name}", mode="elements", strategy="fast")
docs = loader.load()
records=len(docs)

print(f"Hay {docs} documentos a cargar en la colleccion {qdrant_collection}")

qdrant_client = QdrantClient(url=qdrant_url,
                             port=None,
                             api_key=""
                             )
qdrant_client.delete_collection(qdrant_collection)


embeddings = OpenAIEmbeddings(
            openai_api_key=api_key
        )

Qdrant.from_documents(
    docs,
    embeddings,
    url="http://localhost:6333/",
    api_key="",
    port=None,
    collection_name=qdrant_collection

)

