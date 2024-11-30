import os
from PIL import Image

# PARAMETRES :
input_dir = "./original/"
output_dir = "./compressed/"
degree_compress = 20;



def compress_image(image_path, output_path, quality):
    with Image.open(image_path) as img:
        img.save(output_path, quality=quality, optimize=True)


for file in os.listdir(input_dir):
    if file.endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, file)
        output_filename = file # you could modify the output name
        
        output_path = os.path.join(output_dir, output_filename)

        compress_image(input_path, output_path, degree_compress)