import PyPDF2

pdf_file = open('caminho\do\arquivo', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

print(f'Número de páginas: {len(pdf_reader.pages)}')

pagina1 = pdf_reader._get_page(0)

texto_da_pagina = pagina1.extract_text()

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader._get_page(page_num)
    print(f'Conteúdo da página {page_num}: {page.extract_text()}')

pdf_file.close()
