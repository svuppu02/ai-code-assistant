import os
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any, Optional
import hashlib
from langchain.embeddings import OpenAIEmbeddings

from app.core.config import settings


class VectorDBService:
    """Service for managing vector database operations"""

    def __init__(self):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.VECTOR_DB_PATH
        ))
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=settings.OPENAI_API_KEY
        )
        self._initialize_collections()

    def _initialize_collections(self):
        """Initialize collections if they don't exist"""
        try:
            self.code_collection = self.client.get_or_create_collection("code_snippets")
        except Exception as e:
            print(f"Error initializing collections: {e}")

    def _get_hash_id(self, code: str) -> str:
        """Generate a hash ID for a code snippet"""
        return hashlib.md5(code.encode()).hexdigest()

    async def store_code(
            self,
            code: str,
            language: str,
            metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Store code in the vector database"""
        try:
            # Generate a unique ID for the code snippet
            code_id = self._get_hash_id(code)

            # Generate embeddings
            embedding = self.embeddings.embed_query(code)

            # Prepare metadata
            meta = {
                "language": language,
                "length": len(code)
            }
            if metadata:
                meta.update(metadata)

            # Store in collection
            self.code_collection.add(
                ids=[code_id],
                embeddings=[embedding],
                metadatas=[meta],
                documents=[code]
            )

            return code_id

        except Exception as e:
            print(f"Error storing code: {e}")
            raise

    async def search_similar_code(
            self,
            query: str,
            language: Optional[str] = None,
            n_results: int = 5
    ) -> List[Dict[str, Any]]:
        """Search for similar code snippets"""
        try:
            # Generate embeddings for the query
            query_embedding = self.embeddings.embed_query(query)

            # Prepare filters
            filters = {}
            if language:
                filters["language"] = language

            # Search in collection
            results = self.code_collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                where=filters if filters else None
            )

            # Format results
            formatted_results = []
            for i in range(len(results["ids"][0])):
                formatted_results.append({
                    "id": results["ids"][0][i],
                    "code": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if "distances" in results else None
                })

            return formatted_results

        except Exception as e:
            print(f"Error searching code: {e}")
            raise