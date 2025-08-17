from fastapi import FastAPI, UploadFile, File
import PyPDF2
import io
import docx
import re

app = FastAPI()

@app.get("/")
def root():
    return ({"Hello":"World"})

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    # read content of the file
    file_content = await file.read()

    

    #extract text from all pages
    text = ""

    # Resume is pdf type case : 
    if file.filename.endswith(".pdf"):
        #convert bytes into pdf reader
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"


    # Resume is docx type case : 
    elif file.filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(file_content))
        for para in doc.paragraphs:
            text += para.text + "\n"

    # unsupported type
    else:
        return{"error" : "Unsupported file format."}
    
    # Finding out emails and phone no.s with regular expressions
    EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    PHONE_REGEX = r"(?:\+?91[\s-]?)?[6-9]\d{9}"

    emails = re.findall(EMAIL_REGEX, text)
    phones = re.findall(PHONE_REGEX, text)

    # deduping while keeping order
    emails = list(dict.fromkeys([e.strip() for e in emails]))
    phones = list(dict.fromkeys([p.strip() for p in phones]))

    return{
        "filename" : file.filename,
        "emails" : emails,
        "phones" : phones,
        "extracted_text" : text[:500]
    }
