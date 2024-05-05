from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pathlib import Path
import os
import fitz
from docx import Document
import docx2txt
import threading
from urllib.parse import urlparse
import requests
import tempfile

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text_extraction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Flask-Mail for email notifications
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'testingsanket57@gmail.com'
app.config['MAIL_PASSWORD'] = 'vxgp amvu vssq czev'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

class TextExtraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    extracted_text = db.Column(db.Text)
    email = db.Column(db.String(200), index=True)
    
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def extract_text_from_doc(file_path):
    text = docx2txt.process(file_path)
    return text

def send_email_async(email, text):
    msg = Message('Text Extraction Task Completed', sender='testingsanket57@gmail.com', recipients=[email])
    msg.body = text
    mail.send(msg)

def process_document(file_path, email):
    with app.app_context():
        try:
            if urlparse(file_path).scheme in ('http', 'https'):
                response = requests.get(file_path)
                if response.status_code == 200:
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                        temp_file.write(response.content)
                        temp_file_path = temp_file.name
                else:
                    print("Failed to download the file from the URL:", file_path)
                    return
            else:
                temp_file_path = file_path

        
            file_extension = Path(temp_file_path).suffix.lower()
            if file_extension == ".pdf":
                extracted_text = extract_text_from_pdf(temp_file_path)
            elif file_extension == ".docx":
                extracted_text = extract_text_from_docx(temp_file_path)
            elif file_extension == ".doc":
                extracted_text = extract_text_from_doc(temp_file_path)
            else:
                print("Unsupported file type:", file_extension)
                return
        except Exception as e: 
            print("Exception occurs:", e)

        text_extraction = TextExtraction(extracted_text=extracted_text, email=email)
        db.session.add(text_extraction)
        db.session.commit()

        send_email_async(email, extracted_text)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    data = request.json
    email = data.get('email')
    file_path_or_url = data.get('url')

    if urlparse(file_path_or_url).scheme in ('http', 'https'):
        threading.Thread(target=process_document, args=(file_path_or_url, email)).start()
    else:
        threading.Thread(target=process_document, args=(file_path_or_url, email)).start()

    return jsonify({'message':'Document processing started. You will be notified by email when it is completed.'})

if __name__ == '__main__':
    app.run(debug=True)
