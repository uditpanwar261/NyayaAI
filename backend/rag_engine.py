"""
NyayaAI RAG Engine
Retrieval-Augmented Generation using FAISS + SentenceTransformers
"""
import numpy as np
import json
import os
from typing import List, Dict, Any

try:
    from sentence_transformers import SentenceTransformer
    import faiss
    RAG_AVAILABLE = True
except ImportError:
    RAG_AVAILABLE = False

from clause_db import ALL_CLAUSES, CLAUSE_DATABASE


class NyayaRAGEngine:
    """
    RAG Engine for NyayaAI legal document generation.
    Uses SentenceTransformers for semantic embeddings and FAISS for fast retrieval.
    """

    def __init__(self):
        self.model = None
        self.index = None
        self.clauses = ALL_CLAUSES
        self.embeddings = None
        self._initialized = False

    def initialize(self):
        """Initialize the RAG engine - load model and build FAISS index."""
        if self._initialized:
            return True
        if not RAG_AVAILABLE:
            print("[RAG] sentence-transformers/faiss not available, using keyword fallback")
            return False
        try:
            print("[RAG] Loading SentenceTransformer model...")
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            print("[RAG] Building FAISS index...")
            texts = [f"{c['title']} {c['text']} {c.get('act','')} {c.get('category','')}" for c in self.clauses]
            self.embeddings = self.model.encode(texts, show_progress_bar=False)
            self.embeddings = self.embeddings.astype('float32')
            faiss.normalize_L2(self.embeddings)
            dim = self.embeddings.shape[1]
            self.index = faiss.IndexFlatIP(dim)
            self.index.add(self.embeddings)
            self._initialized = True
            print(f"[RAG] ✅ Indexed {len(self.clauses)} clauses, dim={dim}")
            return True
        except Exception as e:
            print(f"[RAG] Init failed: {e}, using keyword fallback")
            return False

    def retrieve(self, query: str, doc_type: str = None, top_k: int = 5) -> List[Dict]:
        """
        Retrieve top-k relevant clauses for a given query.
        Falls back to keyword matching if FAISS is unavailable.
        """
        if self._initialized and self.model and self.index:
            return self._faiss_retrieve(query, doc_type, top_k)
        return self._keyword_retrieve(query, doc_type, top_k)

    def _faiss_retrieve(self, query: str, doc_type: str, top_k: int) -> List[Dict]:
        """Semantic retrieval using FAISS."""
        try:
            query_vec = self.model.encode([query]).astype('float32')
            faiss.normalize_L2(query_vec)
            scores, indices = self.index.search(query_vec, top_k * 3)
            results = []
            seen = set()
            for i, idx in enumerate(indices[0]):
                if idx < 0 or idx >= len(self.clauses):
                    continue
                clause = self.clauses[idx]
                # Prioritize clauses matching doc_type
                if doc_type and clause.get('doc_type') not in [doc_type, 'general']:
                    continue
                if clause['id'] not in seen:
                    seen.add(clause['id'])
                    results.append({**clause, 'relevance_score': float(scores[0][i])})
                if len(results) >= top_k:
                    break
            # Fill with general clauses if needed
            if len(results) < top_k:
                for clause in self.clauses:
                    if clause.get('doc_type') == 'general' and clause['id'] not in seen:
                        seen.add(clause['id'])
                        results.append({**clause, 'relevance_score': 0.5})
                    if len(results) >= top_k:
                        break
            return results
        except Exception as e:
            print(f"[RAG] FAISS search error: {e}")
            return self._keyword_retrieve(query, doc_type, top_k)

    def _keyword_retrieve(self, query: str, doc_type: str, top_k: int) -> List[Dict]:
        """Keyword-based fallback retrieval."""
        query_lower = query.lower()
        query_words = set(query_lower.split())
        scored = []
        for clause in self.clauses:
            text = f"{clause['title']} {clause['text']} {clause.get('category','')}".lower()
            score = sum(1 for w in query_words if w in text)
            # Boost doc_type match
            if doc_type and clause.get('doc_type') == doc_type:
                score += 3
            elif clause.get('doc_type') == 'general':
                score += 1
            scored.append((score, clause))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [{**c, 'relevance_score': s/10} for s, c in scored[:top_k]]

    def get_clauses_for_document(self, doc_type: str) -> List[Dict]:
        """Get all clauses for a specific document type + general clauses."""
        specific = [c for c in self.clauses if c.get('doc_type') == doc_type]
        general = [c for c in self.clauses if c.get('doc_type') == 'general']
        return specific + general

    def build_rag_context(self, doc_type: str, user_inputs: Dict) -> str:
        """Build a context string from retrieved clauses for LLM generation."""
        query = f"{doc_type} {' '.join(str(v) for v in user_inputs.values())}"
        clauses = self.retrieve(query, doc_type, top_k=8)
        context_parts = ["RETRIEVED LEGAL CLAUSES FROM INDIAN LAW DATABASE:\n"]
        for i, clause in enumerate(clauses, 1):
            context_parts.append(
                f"{i}. [{clause['title']}]\n"
                f"   Act: {clause.get('act','Indian Contract Act, 1872')}\n"
                f"   Text: {clause['text']}\n"
            )
        return "\n".join(context_parts)


# Global RAG instance
rag_engine = NyayaRAGEngine()
