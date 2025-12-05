from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader(input("Enter the path where the file is in: "))

total_pages = len(reader.pages)

for i in range(total_pages):
	writer = PdfWriter()
	writer.add_page(reader.pages[i])

	output_name = f"page_{i+1}.pdf"

	with open(output_name, "wb") as output_file:
		writer.write(output_file)
print(f"file split into {total_pages} pages")
