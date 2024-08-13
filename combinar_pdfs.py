import PyPDF2
import os
import getpass

username = getpass.getuser() 

input_dir = f'C:/Users/{username}/Desktop/PDF/DataIn/'
output_dir = f'C:/Users/{username}/Desktop/PDF/DataOut/'
output_path = os.path.join(output_dir, 'PDFGenerado.pdf')

os.makedirs(output_dir, exist_ok=True)

pdf_writer = PyPDF2.PdfWriter()

for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(input_dir, filename)
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

with open(output_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print(f'PDFs combinados exitosamente en: {output_path}')