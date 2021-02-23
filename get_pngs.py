import cairosvg
import os 

# parent_width=None, parent_height=None, dpi=None, scale=None

for file in os.listdir("./icons/svg"):
	if file.endswith(".svg"):
		file_path = "./icons/svg/" + file
		write_path = "./icons/png/" + os.path.splitext(file)[0] + '.png'
		cairosvg.svg2png(url=file_path, write_to=write_path)