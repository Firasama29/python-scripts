import html2text

def convert_html_to_markdown(input_file, output_file):
	
	# read input file
	with open(input_file, 'r', encoding='utf-8') as f:
		html_content = f.read()
		
		
	# converter
	converter = html2text.HTML2Text()
	converter.ignore_links = False
	converter.ignore_images = False
	converter.body_width = 0
	
	
	# convert
	markdown = converter.handle(html_content)
	
	# save to output file
	with open(output_file, 'w', encoding='utf-8') as f:
		f.write(markdown)
		
		
	print(f"{input_file} converted successfully: {output_file}")
	
	
if __name__ == "__main__":
	convert_html_to_markdown("./input_html_file.html", "./output_markdown_file.md")
