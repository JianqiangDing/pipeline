import bpy, bmesh


def set_surrounding_box(location, rotation, size, bevel_width=0, bevel_segments=10):
    # add a new cube
    bpy.ops.mesh.primitive_cube_add(location=location, rotation=rotation, size=size)
    surrounding_box = bpy.context.object
    surrounding_box.name = 'surrounding_box'
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(surrounding_box.data)
    vs = [v for v in bm.verts if v.index == 5]
    bmesh.ops.delete(bm, geom=vs, context='VERTS')
    bmesh.update_edit_mesh(surrounding_box.data)
    bpy.ops.object.mode_set(mode='OBJECT')
    # add bevel modifier
    bevel_modifier = surrounding_box.modifiers.new(type='BEVEL', name='surrounding_box_bevel')
    bevel_modifier.width = bevel_width
    bevel_modifier.segments = bevel_segments
    return surrounding_box
