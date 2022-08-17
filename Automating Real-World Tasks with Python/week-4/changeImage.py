#!/usr/bin/env python3

from PIL import Image
from os import listdir, path, getcwd
from multiprocessing import Pool, cpu_count

file_extension  = ".jpeg"
img_type_market = "JPEG"
files_path      = getcwd() + "/supplier-data/images/"
files           = listdir(files_path)
pool            = Pool(cpu_count())

def update_image(file):
    file = files_path + file

    if path.isfile(file) and '.tiff' in file:
        try:
            im = Image.open(file)
            file_name = path.splitext(path.basename(file))[0]
            im.convert("RGB").resize((600,400)).save(files_path + file_name + file_extension, img_type_market)
            im.close()
        except Exception as e:
            print(e)

for file in files:
    update_image(file)