import bpy
import numpy as np


def load_obj(path, location, rotation_euler, scale):
    x = rotation_euler[0] * 1.0 / 180.0 * np.pi
    y = rotation_euler[1] * 1.0 / 180.0 * np.pi
    z = rotation_euler[2] * 1.0 / 180.0 * np.pi
    prev = []
    for ii in range(len(list(bpy.data.objects))):
        prev.append(bpy.data.objects[ii].name)
    bpy.ops.import_scene.obj(filepath=path, axis_forward='Y', axis_up='Z')
    after = []
    for ii in range(len(list(bpy.data.objects))):
        after.append(bpy.data.objects[ii].name)
    name = list(set(after) - set(prev))[0]
    obj = bpy.data.objects[name]
    obj.location = location
    obj.rotation_euler = [x, y, z]
    obj.scale = scale
    bpy.context.view_layer.update()
    return obj
