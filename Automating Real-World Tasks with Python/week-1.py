#!/usr/bin/env python3

from PIL import Image
from os import listdir, path, getcwd
from multiprocessing import Pool, cpu_count

save_path       = "/opt/icons/"
file_extension  = ".jpeg"
img_type_market = "JPEG"
files_path      = getcwd() + "/images/"
files           = listdir(files_path)
pool            = Pool(cpu_count())

def update_image(file):
    if '.DS' not in file:
        try:
            im = Image.open(files_path + file)
            file_name = path.basename(files_path + file)
            im.convert("RGB").rotate(-90).resize((128,128)).save(save_path + file_name + file_extension, img_type_market)
            im.close()
        except Exception as e:
            print(e)

pool.map(update_image, files)