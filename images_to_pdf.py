from PIL import Image
import os

folder = input("Enter the folder containing images: ")
output_pdf = input("Enter the output PDF name: ")

images = []

for file in os.listdir(folder):
	if file.lower().endswith((".jpeg", ".jpg", ".png")):
		image = Image.open(os.path.join(folder, file)).convert("RGB")
		images.append(image)

if images:
	first_image = images[0]
	others = images[1:]
	first_image.save(output_pdf, save_all=True, append_images=others)
	print("Images merged into one PDF successfully")
else:
	print("No valid images found")
