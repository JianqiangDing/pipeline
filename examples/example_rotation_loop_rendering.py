import os
import sys
import numpy as np

sys.path.append('../pipeline')  # ensure python can find the PIPELINE module

import pipeline as pl

"""
1. ENSURE BLENDER executable program already added in your system PATH, especially when you working on Windows
    a. so that we can call blender from any terminal just by executing the following command
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
5. Seconds or minutes later, the rendered images shall be stored in the a subdirectory inside the 'results' directory finally
6 . GOOD LUCK :) 
"""

if __name__ == '__main__':
    working_dir = os.getcwd()
    results_dir = 'results'
    output_proj_name = 'proj.blend'
    output_images_dir = os.path.join(working_dir, results_dir, pl.func.time_stamp())
    output_proj_path = os.path.join(working_dir, results_dir, output_proj_name)
    # init blender
    image_width, image_height = 400, 400
    samples_num = 30
    exposure = 1.0
    pl.render.init.set_blender(image_width, image_height, samples_num, exposure, use_both_cpu_gpu=True)
    # init wire
    wire_path = './data/white_house_20210407_204933.obj'
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
    pl.render.material.set_material_plastic(wire, wire_color, 0.5)
    # set invisible plane as background
    pl.render.env.set_invisible_ground(location=(0, 0, -1))
    # set camera
    cam = pl.render.camera.set_camera_orthogonal((0, 0, 2), (0, 0, 0), 1, -1, -1, 1)
    # set sun light
    sun_lt = pl.render.light.set_light_sun((0, 0, 3), (0, 0, 180), 2, 1, cast_shadow=False, shadow_soft_size=0)
    # save the blender project
    pl.render.oi.save_proj(output_proj_path, remove_if_exists=True)
    # sat the animation
    pl.render.animation.set_animation()
    stop_frames = 10
    rotation_frames = 30
    total_frames = 0
    data_path = 'rotation_euler'
    # top
    pl.render.animation.set_frame(total_frames)
    wire.rotation_euler = [0.0, 0.0, 0.0]
    pl.render.animation.insert_frame(wire, data_path)
    # stop
    total_frames += stop_frames
    pl.render.animation.set_frame(total_frames)
    pl.render.animation.insert_frame(wire, data_path)
    # front
    total_frames += rotation_frames
    pl.render.animation.set_frame(total_frames)
    wire.rotation_euler.x = -90.0 / 180.0 * np.pi
    pl.render.animation.insert_frame(wire, data_path)
    # stop
    total_frames += stop_frames
    pl.render.animation.set_frame(total_frames)
    pl.render.animation.insert_frame(wire, data_path)
    # right
    total_frames += rotation_frames
    pl.render.animation.set_frame(total_frames)
    wire.rotation_euler.x = 0.0
    wire.rotation_euler.y = -90.0 / 180.0 * np.pi
    pl.render.animation.insert_frame(wire, data_path)
    # stop
    total_frames += stop_frames
    pl.render.animation.set_frame(total_frames)
    pl.render.animation.insert_frame(wire, data_path)
    # back to front
    total_frames += rotation_frames
    pl.render.animation.set_frame(total_frames)
    wire.rotation_euler.x = -90.0 / 180.0 * np.pi
    wire.rotation_euler.y = 0.0
    pl.render.animation.insert_frame(wire, data_path)
    # stop
    total_frames += stop_frames
    pl.render.animation.set_frame(total_frames)
    pl.render.animation.insert_frame(wire, data_path)
    # back to top
    total_frames += rotation_frames
    pl.render.animation.set_frame(total_frames)
    wire.rotation_euler.x = 0.0
    pl.render.animation.insert_frame(wire, data_path)
    # rendering
    pl.render.run.animation_rendering(output_images_dir, cam, total_frames, 0, total_frames)
