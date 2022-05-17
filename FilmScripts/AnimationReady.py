import bpy

C = bpy.context

for ob in C.selected_objects:
    print(ob.name)
