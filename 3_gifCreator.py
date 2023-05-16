import os
import imageio
from tqdm import tqdm
from argparse import ArgumentParser

def gifCreator(dir, output_dir = 'out.gif', fps = 1):
    print('=' * 60)
    print(' - Processing starts -')
    imgs = []
    loader = tqdm(os.listdir(dir))
    for img in loader:
        loader.set_description(f' - GIF Creator ')
        imgs.append(imageio.imread(dir + img))
        loader.set_postfix(file = img)
    imageio.mimsave(output_dir, imgs , fps = fps)
    print(f' - Processing successfully finished. GIF saved to {output_dir} - ')
    print('=' * 60)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--DIR', help = 'direction to images', type = str, default='gifCreator/images/')
    parser.add_argument('--OUTPUT_DIR', help = 'output direction', type = str, default='gifCreator/out.gif')
    parser.add_argument('--FPS', help = 'determine the fps value', type=float, default=1.0)     # less -> slow
    args = parser.parse_args()
    
    gifCreator(dir = args.DIR, output_dir = args.OUTPUT_DIR, fps = args.FPS)