from pypdf import PdfReader

def extract_text(pdf_doc): # To extract the raw text from the input pdf
    try:
        pdf = PdfReader(pdf_doc)

        raw_text = ""

        for index, page in enumerate(pdf.pages):
            # Get by index and respective pages in pdf
            text = page.extract_text() # To get only text from each pages
            if text: # If pages contains text it will get added to raw text
                raw_text += text

        return raw_text  # ✅ correctly aligned

    except Exception as e: # Error for unexpected file
        print(f"Error extracting text from PDF: {e}")
        return None