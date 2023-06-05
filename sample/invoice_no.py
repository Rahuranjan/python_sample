import re
import PyPDF2

def extract_invoice_info(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page_content = ""
        for page in reader.pages:
            page_content += page.extract_text()

    invoice_pattern = r'Invoice Number:\s*(\w+)'  
    invoice_adresses = re.findall(invoice_pattern, page_content)

    return invoice_adresses 
    
if __name__ == '__main__':
    invoices = extract_invoice_info('bill.pdf')

    for invoice in invoices:
        print(invoice)