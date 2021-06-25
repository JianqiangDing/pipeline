import bpy


def animation_rendering(out_dir, camera, duration, frame_start, frame_end):
    assert 0 <= frame_start <= frame_end <= duration
    bpy.data.scenes['Scene'].render.filepath = out_dir if out_dir.endswith('\\') else out_dir + '\\'
    bpy.data.scenes['Scene'].camera = camera
    bpy.data.scenes['Scene'].frame_start = frame_start
    bpy.data.scenes['Scene'].frame_end = frame_end
    bpy.data.scenes['Scene'].frame_current = frame_start
    bpy.ops.render.render(animation=True)
