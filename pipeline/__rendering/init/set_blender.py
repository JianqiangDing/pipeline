import bpy


def set_blender(width, height, samples_num=128, exposure=1.5, use_both_cpu_gpu=False):
    # clear all
    bpy.ops.wm.read_homefile()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    # use cycle
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.resolution_x = width
    bpy.context.scene.render.resolution_y = height
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.cycles.samples = samples_num
    bpy.context.scene.cycles.max_bounces = 6
    bpy.context.scene.cycles.film_exposure = exposure
    bpy.data.scenes[0].view_layers['View Layer']['cycles']['use_denoising'] = 1
    # set devices
    cyclepref = bpy.context.preferences.addons['cycles'].preferences
    cyclepref.compute_device_type = 'CUDA'
    for dev in cyclepref.devices:
        if dev.type == "CPU" and use_both_cpu_gpu is False:
            dev.use = False
        else:
            dev.use = True
    bpy.context.scene.cycles.device = 'GPU'
