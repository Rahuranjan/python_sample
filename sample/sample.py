# import PyPDF2

# def extract_text_from_pdf(pdf_file: str) -> list[str]:
#     with open(pdf_file, 'rb') as pdf:
#         reader = PyPDF2.PdfReader(pdf)
#         pdf_text = []

#         for i in range(0,len(reader.pages)):
#             context = reader.pages[i].extract_text()
#             pdf_text.append(context)

#         return pdf_text
    
# if __name__ == '__main__':
#     extract_text = extract_text_from_pdf('java_interview_question.pdf')

#     for text in extract_text:
#         print(text)

import re
# import PyPDF2
# from pypdf import PdfReader
import pypdf

def extract_text_from_pdf(pdf_file) :
    with open(pdf_file, 'rb') as pdf:
        reader = pypdf.PdfReader(pdf)
        pdf_text = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            pdf_text.append(text)

        return pdf_text
    
if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('java_interview_question.pdf')
    count = 0

    for text in extracted_text:
        split_message = re.split(r'\s+|[,;?.-]\s*', text.lower())

        # print(text)

        if 'oop' in split_message:
            count +=1

    print (count)
    
