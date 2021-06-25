from moviepy.editor import VideoFileClip


def video2gif(video_path, gif_path, suffix=('.mp4', '.mov', '.avi', '.webm'), fps=24):
    assert video_path.endswith(suffix) and fps > 0
    video = VideoFileClip(video_path)
    video.write_gif(gif_path, fps=fps)
