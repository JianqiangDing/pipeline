import os
from PIL import Image


def images2gif(images_dir, gif_name='GIF', suffix=('.png', '.jpg', '.jpeg'), fps=24):
    assert suffix and fps > 0
    images_names = os.listdir(images_dir)
    images_names.sort()
    frames = []
    for image_name in images_names:
        if image_name.endswith(suffix):
            image_path = os.path.join(images_dir, image_name)
            image = Image.open(image_path)
            # TODO some operations, for example handle the transparency
            if image.mode == 'RGBA':
                mask = Image.new('RGBA', image.size, (255, 255, 255, 0))
                frames.append(Image.alpha_composite(mask, image))
            else:
                frames.append(image)
    gif_path = os.path.join(images_dir, gif_name + '.gif')
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=1000 // fps, transparency=0, loop=0,
                   disposal=2)
