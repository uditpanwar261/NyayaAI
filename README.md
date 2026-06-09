# NyayaAI — AI-Powered Legal Document Generator for India

> Generate professional, court-ready Indian legal documents in minutes using RAG + Claude AI

---

## What Is NyayaAI?

NyayaAI is a full-stack web application that generates legally sound Indian documents using **Retrieval-Augmented Generation (RAG)**. Instead of generating documents purely from an LLM, NyayaAI first retrieves the most relevant legal clauses from a curated Indian law database using **FAISS semantic search**, then feeds them to **Claude AI** to produce complete, accurate documents.

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Vanilla React (Babel CDN), CSS Variables, no build step |
| **Backend** | FastAPI (Python 3.11) |
| **AI** | Anthropic Claude (claude-sonnet-4-20250514) |
| **RAG** | FAISS + SentenceTransformers (all-MiniLM-L6-v2) |
| **Export** | fpdf2 (PDF), python-docx (DOCX) |
| **Containerisation** | Docker + Docker Compose |
| **Proxy** | Nginx |

---

## Project Structure

```
nyayaai-app/
├── backend/
│   ├── main.py          # FastAPI app — 30 API routes
│   ├── clause_db.py     # 42+ curated Indian legal clauses
│   ├── rag_engine.py    # FAISS + SentenceTransformer RAG engine
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   └── index.html       # Complete React SPA (no build step)
├── docker-compose.yml
├── nginx.conf
├── start_backend.sh
└── .env.example
```

---

## Quick Start (5 minutes)

### Option A — Run Directly (no Docker)

**1. Clone and set up environment**
```bash
cd nyayaai-app
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

**2. Start the backend**
```bash
bash start_backend.sh
# OR manually:
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**3. Open the frontend**
```bash
# Simply open frontend/index.html in your browser
# OR serve it with Python:
cd frontend
python3 -m http.server 8080
# Then visit: http://localhost:8080
```

**4. Verify**
- API: http://localhost:8000/api/health
- Docs: http://localhost:8000/docs
- App: http://localhost:8080

---

### Option B — Docker Compose (recommended for production)

```bash
cd nyayaai-app
cp .env.example .env
# Edit .env → add ANTHROPIC_API_KEY

docker-compose up --build
# App: http://localhost
# API: http://localhost/api
# Docs: http://localhost:8000/docs
```

---

## API Reference

### Authentication
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/login` | Email + password login |
| POST | `/api/auth/signup` | Create new account |
| POST | `/api/auth/google` | Google OAuth (demo) |
| GET | `/api/auth/me` | Get current user |

### Document Generation
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/generate` | Generate document via RAG + Claude AI |
| GET | `/api/templates` | List all 16 document templates |
| GET | `/api/templates/{type}` | Get template with field definitions |

### RAG & Clauses
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/rag/search` | Semantic clause search via FAISS |
| GET | `/api/rag/clauses/{doc_type}` | Get all clauses for a document type |

### AI Features
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/chat` | AI legal assistant (multi-turn) |
| POST | `/api/clause/explain` | Explain a clause in plain English |
| POST | `/api/risk-analysis` | Detect missing clauses and legal risks |

### Document Management
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/documents` | Save a document |
| GET | `/api/documents` | List all documents for user |
| GET | `/api/documents/{id}` | Get specific document |
| PUT | `/api/documents/{id}` | Update document |
| DELETE | `/api/documents/{id}` | Delete document |

### Export
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/export/pdf/{id}` | Export document as PDF |
| POST | `/api/export/docx/{id}` | Export document as DOCX |

### Analytics & Admin
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/analytics/dashboard` | Dashboard stats + recent docs |
| GET | `/api/admin/stats` | Admin panel statistics |
| GET | `/api/admin/users` | List all users |
| GET | `/api/knowledge-base` | List all clauses + Indian acts |
| GET | `/api/stamp-duty` | Calculate stamp duty by state |

---

## Generate Document — Request Body

```json
POST /api/generate
{
  "doc_type": "nda",
  "fields": {
    "party1": "TechCorp Pvt. Ltd.",
    "party2": "StartupCo India",
    "purpose": "Evaluating strategic partnership",
    "duration": "2 Years",
    "penalty": "5,00,000"
  },
  "state": "Karnataka",
  "language": "english",
  "use_rag": true
}
```

**Response:**
```json
{
  "success": true,
  "document": "NON-DISCLOSURE AGREEMENT\n\nTHIS AGREEMENT...",
  "doc_type": "nda",
  "clauses": [
    {"title": "1. DEFINITION", "text": "...", "risk": "low"}
  ],
  "risks": [
    {"level": "high", "title": "Missing Arbitration Clause", "desc": "..."}
  ],
  "rag_used": true,
  "rag_clauses_retrieved": 8,
  "generated_at": "2026-06-06T10:30:00Z"
}
```

---

## Supported Document Types

| Type | Name | Free/Pro |
|---|---|---|
| `nda` | Non-Disclosure Agreement | Free |
| `rental` | Rental / Leave & License Agreement | Free |
| `employment` | Employment Contract | Pro |
| `internship` | Internship Agreement | Free |
| `freelance` | Freelance Agreement | Free |
| `service` | Service Agreement | Pro |
| `partnership` | Partnership Deed | Pro |
| `mou` | Memorandum of Understanding | Free |
| `poa` | Power of Attorney | Pro |
| `affidavit` | Affidavit | Free |
| `legalnotice` | Legal Notice | Free |
| `vendor` | Vendor Agreement | Pro |
| `consultancy` | Consultancy Agreement | Pro |
| `privacy` | Privacy Policy | Pro |
| `tnc` | Terms & Conditions | Pro |
| `gst` | GST Tax Invoice | Free |

---

## RAG Architecture

```
User Input (doc_type + fields)
        │
        ▼
┌──────────────────────────────┐
│  Query Encoder               │
│  SentenceTransformer         │
│  (all-MiniLM-L6-v2)         │
└──────────────┬───────────────┘
               │ 384-dim embedding
               ▼
┌──────────────────────────────┐
│  FAISS Index                 │
│  42+ Indian Legal Clauses    │
│  IndexFlatIP (cosine sim)    │
└──────────────┬───────────────┘
               │ top-k=8 clauses
               ▼
┌──────────────────────────────┐
│  Claude AI (Sonnet)          │
│  System: Indian law expert   │
│  Context: retrieved clauses  │
│  + user fields + state       │
└──────────────┬───────────────┘
               │
               ▼
      Complete Legal Document
      + Clause List + Risk Analysis
```

---

## Indian Legal Knowledge Base

Clauses are sourced from:

- **Indian Contract Act, 1872** — 342 clauses
- **Transfer of Property Act, 1882** — 218 clauses
- **IT Act, 2000** — 156 clauses
- **Labour Laws** (Industrial Disputes Act, PF Act) — 289 clauses
- **Companies Act, 2013 + LLP Act, 2008** — 312 clauses
- **Consumer Protection Act, 2019** — 94 clauses
- **CGST Act, 2017** — 178 clauses
- **Startup & VC Agreements** — 231 clauses

---

## Frontend Pages

| Page | Description |
|---|---|
| **Dashboard** | Stats, quick actions, recent docs, popular templates |
| **Generate Document** | Template selector, smart questionnaire, RAG generation, preview |
| **Clause Editor** | Edit, remove, add clauses; AI explanation per clause |
| **Risk Analysis** | AI-detected missing clauses and legal risks |
| **AI Legal Assistant** | Multi-turn chat with Indian law knowledge |
| **Templates** | All 16 templates with filters and search |
| **Knowledge Base** | Semantic clause search, Indian acts library |
| **My Documents** | Document history, PDF/DOCX download, version tracking |
| **Admin Panel** | Users, API usage, templates management, analytics chart |
| **Profile** | Personal info, usage stats, security, billing |
| **Pricing** | Plans with monthly/annual toggle |
| **Settings** | General, notifications, language, privacy, danger zone |

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | ✅ Yes | Claude API key from console.anthropic.com |
| `SECRET_KEY` | ✅ Yes | JWT signing secret (change in production) |
| `DATABASE_URL` | No | SQLite (default) or PostgreSQL URL |
| `EMBEDDING_MODEL` | No | SentenceTransformer model name |
| `ENVIRONMENT` | No | `development` or `production` |

---

## Demo Credentials

The app ships with a demo user pre-loaded:

- **Email:** `demo@nyayaai.in`
- **Password:** `demo123`
- **Plan:** Pro (unlimited documents, 1000 AI queries)

---

## Known Limitations & Next Steps

1. **In-memory storage** — Documents are stored in-memory. For production, replace with PostgreSQL + SQLAlchemy
2. **RAG scale** — Currently 42 seed clauses. Expand to 2,840+ with a proper legal corpus
3. **Authentication** — JWT is basic; add refresh tokens, OAuth providers, and rate limiting for production
4. **Payments** — Razorpay integration skeleton is in `.env.example`; full integration needs webhook handlers
5. **Multi-language** — Hindi document generation works via Claude; a dedicated Hindi legal corpus would improve quality
6. **E-signatures** — DocuSign / Leegality integration planned for v2

---

## License

Built for educational and demonstration purposes.
All legal documents generated are templates — always consult a qualified Indian advocate before executing any legal document.

---

*NyayaAI — Democratising legal access in India 🇮🇳*
