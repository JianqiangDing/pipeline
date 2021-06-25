import bpy
import numpy as np


def set_mask_plane(location=(0, 0, 0), rotation_euler=(0, 0, 0), size=20, hole_radius=10):
    # init a plane
    bpy.ops.mesh.primitive_plane_add(size=size)
    plane = bpy.context.object
    plane.name = 'plane_with_hole'
    # init a cylinder
    bpy.ops.mesh.primitive_cylinder_add(vertices=100, radius=hole_radius)
    cylinder = bpy.context.object
    bpy.ops.object.select_all(action='DESELECT')
    # add boolean difference modifier
    diff_mod = plane.modifiers.new(name='bool_diff', type='BOOLEAN')
    diff_mod.operation = 'DIFFERENCE'
    diff_mod.object = cylinder
    # must active the plane before boolean operation
    bpy.context.view_layer.objects.active = plane
    bpy.ops.object.modifier_apply(modifier=diff_mod.name)
    # remove the cylinder
    bpy.ops.object.select_all(action='DESELECT')
    cylinder.select_set(True)
    bpy.ops.object.delete()
    # now transform the resulting plane
    plane.location = location
    x = rotation_euler[0] * 1.0 / 180.0 * np.pi
    y = rotation_euler[1] * 1.0 / 180.0 * np.pi
    z = rotation_euler[2] * 1.0 / 180.0 * np.pi
    plane.rotation_euler = (x, y, z)
