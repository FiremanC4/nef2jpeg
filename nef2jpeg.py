from imageio import imsave
from rawpy import imread
from os import makedirs
from sys import argv
from tqdm import tqdm
from glob import glob

FOLDER = (argv + ['JPEG'])[1]
makedirs(FOLDER, exist_ok=True)

for i in tqdm(glob("*.NEF"), unit='file'):
    with imread(i) as raw: rgb = raw.postprocess(use_camera_wb=True)
    imsave(f'{FOLDER}\\' + i[:-3] + 'jpg', rgb)

input('DONE! Press ENTER to exit... ')