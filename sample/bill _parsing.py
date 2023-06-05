import os
import PyPDF2

dir_path = r'C:\Users\rahur\Downloads\Bills'
os.chdir(dir_path)

file_list = os.listdir()

for file_name in file_list:

    f = open(os.path.join(dir_path, file_name), 'rb')
    reader = PyPDF2.PdfReader(f)
    file_content = reader.pages[0].extract_text().split('\n')
    invoice_no = ""
    date = ""
    amount = ""

    for i in range(len(file_content)):
        
        if "Invoice Number" in file_content[i]:
            invoice_no = file_content[i].split(':')[0]

        # if file_content[i].find('Invoice Date') != -1:
        #     date = file_content[i].split(':')[1]
            
        # if file_content[i].find("Gross Amount") != -1:
        #     amount = file_content[i+1].split(' ')[0]

    print(invoice_no )