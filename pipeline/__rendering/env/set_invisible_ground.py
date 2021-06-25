import bpy


def set_invisible_ground(location=(0, 0, 0), size=20, shadow_brightness=0.7):
    # initialize a ground for shadow
    bpy.context.scene.cycles.film_transparent = True
    bpy.ops.mesh.primitive_plane_add(location=location, size=size)
    bpy.context.object.cycles.is_shadow_catcher = True
    #  set material
    ground = bpy.context.object
    mat = bpy.data.materials.new('MeshMaterial')
    ground.data.materials.append(mat)
    mat.use_nodes = True
    tree = mat.node_tree
    tree.nodes["Principled BSDF"].inputs['Transmission'].default_value = shadow_brightness
