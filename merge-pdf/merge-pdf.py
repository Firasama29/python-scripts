from PyPDF2 import PdfMerger
import os

folder = "/home/firas/Documents/test"
output_file = "/home/firas/Documents/test/merged_pdf.pdf"

merger = PdfMerger()

# merge
for file in os.listdir(folder):
	if file.endswith('.pdf'):
		merger.append(os.path.join(folder, file))

# write to output file
merger.write(output_file)
print("file saved")
merger.close()
