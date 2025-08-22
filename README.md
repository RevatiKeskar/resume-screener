# Resume Ultimate 🚀  
**AI-Powered Resume–Job Matcher**  

Resume Ultimate helps recruiters and job seekers cut through the noise.  
Upload a resume, upload a job description, and let AI do the heavy lifting — parsing, embedding, and matching the right candidates to the right roles.  

---

## ✨ Features  
- 📄 **Smart Resume Parsing** → Extracts text from PDF and DOCX files.  
- 🔍 **AI-Powered Matching** → Uses **SentenceTransformer embeddings** for semantic similarity.  
- 🗂 **Persistent Storage** → Stores resume embeddings in **ChromaDB** for fast querying.  
- ⚡ **FastAPI Backend** → Blazing fast APIs for uploading resumes & job descriptions.  
- 🎯 **Top Matches** → Returns the most relevant resumes for a given job description.  

---

## 🛠️ Tech Stack  
- **Backend**: FastAPI  
- **Database**: ChromaDB (persistent client)  
- **Embeddings Model**: all-MiniLM-L6-v2 (Sentence Transformers)  
- **Parsing**: PyPDF2 (PDFs), python-docx (DOCX)  
- **Language**: Python 3.10+  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/resume-ultimate.git
cd resume-ultimate
