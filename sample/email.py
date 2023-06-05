# import re
# import PyPDF2

# def extract_email_addresses(pdf_file):
#     with open(pdf_file, 'rb') as pdf:
#         reader = PyPDF2.PdfReader(pdf)
#         pdf_text = ""

#         for page in reader.pages:
#             pdf_text += page.extract_text()

#     email_pattern = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     email_addresses = re.findall(email_pattern, pdf_text)

#     return email_addresses

# if __name__ == '__main__':
#     extract_mail = extract_email_addresses('java_interview_question.pdf')

#     for email in extract_mail:
#         print(email)

import re
import PyPDF2

def extract_email_addresses(pdf_file):
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = ""

        for page in reader.pages:
            pdf_text += page.extract_text()

    email_pattern = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_addresses = re.findall(email_pattern, pdf_text)

    return email_addresses

if __name__ == '__main__':
    extracted_emails = extract_email_addresses('wordpress.pdf')

    for email in extracted_emails:
        print(email)
