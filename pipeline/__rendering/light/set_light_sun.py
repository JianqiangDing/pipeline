import bpy
import numpy as np


def set_light_sun(location, rot_euler, energy, strength, cast_shadow=True, name='sun_light', shadow_soft_size=0.05):
    x = rot_euler[0] * 1.0 / 180.0 * np.pi
    y = rot_euler[1] * 1.0 / 180.0 * np.pi
    z = rot_euler[2] * 1.0 / 180.0 * np.pi
    sun_lt_data = bpy.data.lights.new(name=name, type='SUN')
    sun_lt = bpy.data.objects.new(name=name, object_data=sun_lt_data)
    bpy.context.collection.objects.link(sun_lt)
    sun_lt.location = location
    sun_lt.rotation_euler = [x, y, z]
    sun_lt.data.angle = shadow_soft_size
    sun_lt.data.energy = energy
    sun_lt.data.cycles.cast_shadow = cast_shadow
    sun_lt.data.use_nodes = True
    sun_lt.data.node_tree.nodes["Emission"].inputs['Strength'].default_value = strength
    return sun_lt
