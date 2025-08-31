import PyPDF2
import os


base_name = "life_3_0_page_"
text_file_directory = 'Text'


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page_num in range(len(reader.pages)):
            if page_num > 10:
                text.append(reader.pages[page_num].extract_text())
        return text
    
pdf_content = extract_text_from_pdf("life_3_0.pdf")


for i in range(len(pdf_content)):
    file_name = f"{base_name}{i+1}.txt"
    file_name = os.path.join(text_file_directory, file_name)
    try:
        with open(file_name, 'x') as file:
            file.write(pdf_content[i])
        print(f"File '{file_name}' created successfully (exclusive mode).")
    except FileExistsError:
        print(f"File '{file_name}' already exists. Not overwritten.")