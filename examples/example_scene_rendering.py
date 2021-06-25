import os
import sys

sys.path.append('../pipeline')  # ensure python can find the PIPELINE module

import pipeline as pl

"""
1. ENSURE BLENDER executable program already added in your system PATH, especially when you working on Windows
    a. so that we can call blender from any terminal by just typing the following command
    $$ blender 
2. ENSURE all third-party modules already installed for the blender python (PIL and moviepy)
    a. here is a simple solution, cd to the directory where the blender python(.exe) exists 
    i.e. C:\Program Files\Blender Foundation\Blender 2.93\2.93\python\bin
    execute the following command in any terminal you prefer, i.e, cmd or powershell  
        $$ .\python.exe -m pip install [NAME OF THE THIRD-PARTY MODULE]
    i.e $$ .\python.exe -m pip install Pillow moviepy
3. Then run this blender script as usual by executing following command in any terminal you like
        $$ blender -b -P examples_scene_rendering.py
4. Probably you may need to new a directory named 'results' somewhere to store the final results
5. Seconds or minutes later, the rendered image shall be stored in the 'results' directory finally
6 . GOOD LUCK :) 
"""

if __name__ == '__main__':
    working_dir = os.getcwd()
    results_dir = 'results'
    output_image_name = pl.func.time_stamp() + '.png'
    output_proj_name = 'proj.blend'
    output_image_path = os.path.join(working_dir, results_dir, output_image_name)
    output_proj_path = os.path.join(working_dir, results_dir, output_proj_name)
    # init blender
    image_width, image_height = 720, 720
    samples_num = 500
    exposure = 1.0
    pl.render.init.set_blender(image_width, image_height, samples_num, exposure, use_both_cpu_gpu=True)
    # init wire
    wire_path = 'data/angels_2_210421_00.obj'
    location = (0, 0, 0)
    rotation = (0, 0, 0)
    scale = (1, 1, 1)
    wire = pl.render.oi.load_obj(wire_path, location, rotation, scale)
    wire.scale *= 0.5 / max(wire.dimensions)
    # wire to blender curve
    wire = pl.render.geometric.obj2curve(wire)
    wire = pl.render.geometric.curve2mesh(wire, 2, 20)
    # set shading
    pl.render.shading.shade_smooth()
    # subdivision
    pl.render.geometric.mesh_subdivision(wire, 0)
    # set material
    wire_color = pl.render.color.Color(pl.render.color.derek_blue, 0.5, 1.0, 1.0, 0.0, 2.0)
    pl.render.material.set_material_single_color(wire, wire_color, 0.5)
    # set invisible ground
    pl.render.env.set_invisible_ground(location=(0, 0, -5), size=10)
    # set surrounding box
    surrounding_box = pl.render.env.set_surrounding_box(location=(0.5, -0.5, 0.5), rotation=(0, 0, 0), size=2.5)
    surrounding_box_color = pl.render.color.Color(pl.render.color.deco_silver, 0.5, 1.0, 1.0, 0.0, 2.0)
    pl.render.material.set_material_single_color(surrounding_box, surrounding_box_color, 0.5)
    # set camera
    cam_location = (0.8, -0.8, 0.8)
    look_at_pos = (0, 0, 0)
    focal_length = 35
    cam = pl.render.camera.set_camera_perspective(cam_location, look_at_pos, focal_length)
    # set one area light used for show the surrounding box
    area_lt = pl.render.light.set_light_area((2, -2, 2), (0, 0, 0), 10, 100, False, 'area_light', 180)
    # set three directional lights used for constructing shadows
    sun_lt0 = pl.render.light.set_light_sun((0, -4, 0), (90, 0, 0), 5, 5, True, 'sun_light0', 0)
    sun_lt1 = pl.render.light.set_light_sun((4, 0, 0), (0, 90, 0), 5, 5, True, 'sun_light1', 0)
    sun_lt2 = pl.render.light.set_light_sun((0, 0, 4), (0, 0, 0), 5, 5, True, 'sun_light2', 0)
    # set a planes as masks
    pl.render.env.set_mask_plane((0, -2, 0), (90, 0, 0), size=5, hole_radius=0.3)
    pl.render.env.set_mask_plane((2, 0, 0), (0, 90, 0), size=5, hole_radius=0.3)
    pl.render.env.set_mask_plane((0, 0, 2), (0, 0, 0), size=5, hole_radius=0.3)
    # save the blender project
    pl.render.oi.save_proj(output_proj_path, remove_if_exists=True)
    # save the rendered image
    pl.render.run.image_rendering(output_image_path, cam)
