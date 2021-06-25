import bpy


def set_material_metal(mesh, color, ao_strength, metal_val=0.9):
    mat = bpy.data.materials.new('MeshMaterial')
    mesh.data.materials.append(mat)
    mesh.active_material = mat
    mat.use_nodes = True
    tree = mat.node_tree

    # set principled BSDF
    tree.nodes["Principled BSDF"].inputs['Roughness'].default_value = 0.7
    tree.nodes["Principled BSDF"].inputs['Sheen Tint'].default_value = 0
    tree.nodes["Principled BSDF"].inputs['Metallic'].default_value = metal_val

    # add Ambient Occlusion
    tree.nodes.new('ShaderNodeAmbientOcclusion')
    tree.nodes.new('ShaderNodeGamma')
    tree.nodes.new('ShaderNodeMixRGB')
    tree.nodes["Mix"].blend_type = 'MULTIPLY'
    tree.nodes["Gamma"].inputs["Gamma"].default_value = ao_strength
    tree.nodes["Ambient Occlusion"].inputs["Distance"].default_value = 10.0
    tree.nodes["Gamma"].location.x -= 600

    # set color using Hue/Saturation node
    HSVNode = tree.nodes.new('ShaderNodeHueSaturation')
    HSVNode.inputs['Color'].default_value = color.rgba
    HSVNode.inputs['Saturation'].default_value = color.s
    HSVNode.inputs['Value'].default_value = color.v
    HSVNode.inputs['Hue'].default_value = color.h
    HSVNode.location.x -= 200

    # set color brightness/contrast
    BCNode = tree.nodes.new('ShaderNodeBrightContrast')
    BCNode.inputs['Bright'].default_value = color.b
    BCNode.inputs['Contrast'].default_value = color.c
    BCNode.location.x -= 400

    # link all the nodes
    tree.links.new(HSVNode.outputs['Color'], BCNode.inputs['Color'])
    tree.links.new(BCNode.outputs['Color'], tree.nodes['Ambient Occlusion'].inputs['Color'])
    tree.links.new(tree.nodes["Ambient Occlusion"].outputs['Color'], tree.nodes['Mix'].inputs['Color1'])
    tree.links.new(tree.nodes["Ambient Occlusion"].outputs['AO'], tree.nodes['Gamma'].inputs['Color'])
    tree.links.new(tree.nodes["Gamma"].outputs['Color'], tree.nodes['Mix'].inputs['Color2'])
    tree.links.new(tree.nodes["Mix"].outputs['Color'], tree.nodes['Principled BSDF'].inputs['Base Color'])
