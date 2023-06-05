import PyPDF2

a = PyPDF2.PdfReader('java_interview_question.pdf')

# print(a.metadata)

# page = a.pages[5]

print(len(a.pages))

str = ""

for i in range(0, len(a.pages)):
    str += a.pages[i].extract_text()

with open("output.pdf", 'wb') as f:
    f.write(str.encode())