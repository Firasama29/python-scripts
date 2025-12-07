from PIL import Image
import os

input_image = input("Enter the image file path: ")
output_pdf = input("Enter the pdf file name: ")

if not os.path.exists(input_image):
     raise FileNotFoundError(f"{input_image} does not exist!")
elif os.path.exists(output_pdf):
     raise FileExists(f"{output_pdf} already exists!")

image = Image.open(input_image)

image = image.convert("RGB")

image.save(output_pdf)

print("Image converted to PDF successfully")
