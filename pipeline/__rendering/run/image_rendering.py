import bpy


def image_rendering(out_file_path, camera):
    bpy.data.scenes['Scene'].render.filepath = out_file_path
    bpy.data.scenes['Scene'].camera = camera
    bpy.ops.render.render(write_still=True)
