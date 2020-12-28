import PyPDF2 
a = PyPDF2.PdfFileReader(r'C:\Users\adri2\OneDrive\Desktop\menu\JyotiChaurasiaAssignment.pdf')
print(a.documentInfo)
# print(f'Number of pages = {a.getNumPages()}')
# print(f'Any page number = {a.getPage(1)}')
str1 = ""
for i in range(2):
    str1 += a.getPage(i).extractText()

with open ('text.txt', 'w', encoding='utf-8') as f:
    f.write(str1)


