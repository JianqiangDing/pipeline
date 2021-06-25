import bpy
import mathutils
from .set_camera_look_at import *


def set_camera_orthogonal(location, look_at, top, bottom, left, right):
    # scale the resolution y using resolution x
    assert (abs(left - right) > 0)
    assert (abs(top - bottom) > 0)
    aspect_ratio = abs(right - left) * 1.0 / abs(top - bottom)
    bpy.context.scene.render.resolution_y = bpy.context.scene.render.resolution_x / aspect_ratio
    # define the camera
    bpy.ops.object.camera_add(location=location)
    cam = bpy.context.object
    bpy.context.object.data.type = 'ORTHO'
    cam.data.ortho_scale = abs(left - right)
    loc = mathutils.Vector(look_at)
    set_camera_look_at(cam, loc)
    return cam
