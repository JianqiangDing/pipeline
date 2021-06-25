import bpy
import mathutils
from .set_camera_look_at import *


def set_camera_perspective(location, look_at=(0, 0, 0), focal_length=35):
    bpy.ops.object.camera_add(location=location)
    cam = bpy.context.object
    cam.name = "perspective_camera"
    cam.data.lens = focal_length
    loc = mathutils.Vector(look_at)
    set_camera_look_at(cam, loc)
    return cam
