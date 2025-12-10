import os

def rename_in_bulk(directory):
	try:
		# move to target directory
		os.chdir(directory)
		
		# get files from directory
		files = [f for f in os.listdir() if f.endswith((".png", ".jpg", ".jpeg"))]
		
		if not files:
			print("No images were found in this directory")
			return
		
		n = 1	
		# loop through each file
		for old_file in files:
		
			# split into file name and extension
			_, extension = os.path.splitext(old_file)
			
			new_file = f"image_{n}{extension}"
			n += 1
			
			# rename
			os.rename(old_file, new_file)
			print(f"renamed {old_file} -> {new_file}")

		print(f"renaming completed. Files renamed: {n-1}")
		
	except FileNotFoundError:
		print("Directory not found")
	except Exception as e:
		print(f"An unexpected error occured: {e}")

rename_in_bulk(input("Enter directory path: "))
