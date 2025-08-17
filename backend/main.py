from fastapi import FastAPI, UploadFile, File
import PyPDF2
import io
import docx

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
    

    return{
        "filename" : file.filename,
        "extracted_text" : text[:500]
    }
