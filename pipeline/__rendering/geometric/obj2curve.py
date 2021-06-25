import bpy


def obj2curve(obj):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='OBJECT')
    obj.select_set(True)
    bpy.ops.object.convert(target='CURVE')
    return obj
