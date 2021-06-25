import bpy


def curve2mesh(wire, bevel_depth, bevel_resolution):
    bpy.context.view_layer.objects.active = wire
    bpy.ops.object.mode_set(mode='OBJECT')
    wire.select_set(True)
    wire.data.bevel_depth = bevel_depth
    wire.data.bevel_resolution = bevel_resolution
    wire.data.use_fill_caps = True
    return wire
