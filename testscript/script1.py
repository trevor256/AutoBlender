import bpy

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'
bpy.context.scene.cycles.use_preview_denoising = True
bpy.context.scene.cycles.preview_adaptive_threshold = 0.1
bpy.context.scene.cycles.preview_samples = 1024
bpy.context.scene.cycles.use_preview_denoising = True
bpy.context.scene.cycles.use_adaptive_sampling = True
bpy.context.scene.cycles.adaptive_threshold = 0.01
bpy.context.scene.cycles.samples = 4096
bpy.context.scene.cycles.use_denoising = True


bpy.context.scene.render.resolution_x = 2560
bpy.context.scene.render.resolution_y = 1440
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MKV'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'LOSSLESS'
bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'BEST'

