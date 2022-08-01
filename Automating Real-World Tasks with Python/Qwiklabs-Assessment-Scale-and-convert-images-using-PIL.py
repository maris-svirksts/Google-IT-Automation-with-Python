#! python

from PIL import Image
from os import listdir, path, getcwd
from multiprocessing import Pool, cpu_count

files           = listdir()
save_path       = "/opt/icons/"
file_extension  = ".jpeg"
img_type_market = "JPEG"
path            = getcwd() + "/images/"
pool            = Pool(cpu_count())

def update_image(file):
    im = Image.open(path + file)
    file_name, _ = path.splitext(file)

    try:
        im.convert("RGB").rotate(-90).resize((128,128)).save(save_path + file_name + file_extension, img_type_market)
    except Exception as e:
        print(e)

    im.close()

pool.map(update_image, files)