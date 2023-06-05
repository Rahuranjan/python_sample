import pdfplumber

with pdfplumber.open('wordpress.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_tables()

        print(text)