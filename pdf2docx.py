from pdf2docx import Converter
import os

pdf_file = 'backend-resume.pdf'
docx_file = 'backend-resume.docx'
if not os.path.exists(pdf_file):
    raise FileNotFoundError(f"file '{pdf_file}' does not exist")
elif os.path.exists('backend-resume.docx'):
    raise FileExistsError(f"file '{docx_file}' already exists")
else:
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    print('converting to docx..')
cv.close