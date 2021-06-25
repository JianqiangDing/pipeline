import os
from moviepy.editor import ImageSequenceClip


def images2video(images_dir, video_path, fps=24):
    images_names = os.listdir(images_dir)
    images_names.sort()
    images_paths = [os.path.join(images_dir, image_name) for image_name in images_names]
    clip = ImageSequenceClip(images_paths, fps=fps)
    clip.write_videofile(video_path, fps=fps)
