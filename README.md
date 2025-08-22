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

## Getting started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/resume-ultimate.git
cd resume-ultimate
```

### Create & Activate Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the FastAPI Server
```bash
uvicorn main:app --reload
```

API will be live at http://127.0.0.1:8000/docs


## 📌 API Endpoints  

### 📄 Upload Resume  
**POST** `/upload_resume`  
- **Input**: PDF or DOCX file  
- **Action**: Parses, embeds, stores in ChromaDB  

### 📝 Upload Job Description  
**POST** `/upload_job`  
- **Input**: Job description (text file or raw text)  
- **Action**: Embeds JD, queries ChromaDB, returns top matching resumes  

---

## 🌟 Roadmap  
- ✅ Resume parsing & storage  
- ✅ Job description embedding & matching  
- ⬜️ Web UI for easy uploads  
- ⬜️ Advanced filters (skills, experience, location)  
- ⬜️ Deployment on cloud (Azure/GCP/AWS)  

---

## 📜 License  
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  


