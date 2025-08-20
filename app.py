import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import PyPDF2
import io

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_for_dev")

# Configuration
ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_stream):
    """Extract text from PDF file stream using PyPDF2."""
    try:
        pdf_reader = PyPDF2.PdfReader(file_stream)
        text = ""
        
        # Extract text from all pages
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
        return text.strip()
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {str(e)}")
        raise Exception(f"Failed to extract text from PDF: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route for PDF upload and text extraction."""
    extracted_text = None
    filename = None
    
    if request.method == 'POST':
        # Check if file was uploaded
        if 'pdf_file' not in request.files:
            flash('No file selected. Please choose a PDF file to upload.', 'error')
            return redirect(request.url)
        
        file = request.files['pdf_file']
        
        # Check if file was actually selected
        if file.filename == '':
            flash('No file selected. Please choose a PDF file to upload.', 'error')
            return redirect(request.url)
        
        # Validate file type
        if not allowed_file(file.filename):
            flash('Invalid file type. Please upload a PDF file only.', 'error')
            return redirect(request.url)
        
        try:
            # Secure the filename
            filename = secure_filename(file.filename or "uploaded_file.pdf")
            
            # Read file into memory for processing
            file_stream = io.BytesIO(file.read())
            
            # Extract text from PDF
            extracted_text = extract_text_from_pdf(file_stream)
            
            if not extracted_text:
                flash('No text could be extracted from this PDF. The file might be image-based or corrupted.', 'warning')
            else:
                flash(f'Successfully extracted text from "{filename}"', 'success')
                
        except Exception as e:
            logging.error(f"Error processing PDF: {str(e)}")
            flash(f'Error processing PDF: {str(e)}', 'error')
    
    return render_template('index.html', 
                         extracted_text=extracted_text, 
                         filename=filename)

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error."""
    flash('File too large. Please upload a PDF file smaller than 16MB.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
