import bpy
import numpy as np


def set_light_area(location, track_to_pos, energy, strength, cast_shadow=True, name='area_light', spread=180):
    # init area light
    area_lt_data = bpy.data.lights.new(name=name, type='AREA')
    area_lt = bpy.data.objects.new(name=name, object_data=area_lt_data)
    bpy.context.collection.objects.link(area_lt)
    # set location
    area_lt.location = location
    # define an empty object used for tracking to
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=track_to_pos)
    obj_tracking_to = bpy.context.object
    # set tracking to constraint
    tracking_constraint = area_lt.constraints.new('TRACK_TO')
    tracking_constraint.target = obj_tracking_to
    # set params else
    area_lt.data.energy = energy
    area_lt.data.spread = spread
    area_lt.data.cycles.cast_shadow = cast_shadow
    area_lt.data.use_nodes = True
    area_lt.data.node_tree.nodes["Emission"].inputs['Strength'].default_value = strength
    return area_lt
