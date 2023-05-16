import os , sys
from tqdm import tqdm
from PIL import Image
from argparse import ArgumentParser


def jpg2png(jpg_dir, png_dir):
    print('=' * 60)
    print(' - Processing starts -')
    loader = tqdm(os.listdir(jpg_dir))
    for file in  loader:
        if file.split('.')[1] == 'jpg':  
            loader.set_description(f' - JPG -> PNG ')
            img = Image.open(jpg_dir + file ) # Direction Of Input Folder
            img.save(png_dir + file.split('.')[0]+'.png') # Direction Of Output Folder
            loader.set_postfix(file = file)
    print(' - Processing successfully finished - ')
    print('=' * 60)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--JPG_DIR', help = 'The direction of jpg images', type = str, default='jpg2png/jpg/')
    parser.add_argument('--PNG_DIR', help = 'The direction of png images', type = str, default='jpg2png/png/')
    args = parser.parse_args()
    
    jpg2png(args.JPG_DIR, args.PNG_DIR)
