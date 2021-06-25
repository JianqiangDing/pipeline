import bpy
import os


def save_proj(output_proj_path, remove_if_exists=True):
    os.remove(output_proj_path) if os.path.exists(output_proj_path) and remove_if_exists else None
    bpy.ops.wm.save_mainfile(filepath=output_proj_path)
    