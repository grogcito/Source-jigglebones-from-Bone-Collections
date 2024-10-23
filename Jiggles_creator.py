# ---select your armature, enter pose mode, create a bone collection
# ---select the bones and assign them to the collection.
# ---the script will generate a new text file named "Jiggle" inside blender
# ---with all the bones in that collection, ordered by their parenting order

#------NOTE: won't work in edit mode (bone collections are empty in edit mode).
#------switch to object or pose mode, keep your armature selected.

import bpy
import mathutils

bloque_texto = bpy.data.texts.get("Jiggle")
if bloque_texto : bloque_texto.clear() 
else : bloque_texto = bpy.data.texts.new(name="Jiggle")

coleccionHuesos = bpy.context.object.data.collections.active
#bpy.context.object.data.collections.active.bones['Tail2'].head_local
#print(bpy.context.object.data.name)

for bone in coleccionHuesos.bones:
    print(bone.name)
    n = coleccionHuesos.bones.keys().index(bone.name)
    boneStart = coleccionHuesos.bones[n].head_local
    boneStartname = coleccionHuesos.bones[n].name
    
    if coleccionHuesos.bones[n].children.keys():
        print('yes')
        if n == len(coleccionHuesos.bones) - 1:
            #boneStart = coleccionHuesos.bones[n].head_local
            boneEnd   = coleccionHuesos.bones[n].head_local
            boneEndname = coleccionHuesos.bones[n].name
            boneLength = (boneStart - boneEnd).length
        else: boneEnd   = coleccionHuesos.bones[n+1].head_local
        boneEndname = coleccionHuesos.bones[n+1].name
        boneLength = (boneStart - boneEnd).length
    else: print('no')
    
    print(n,boneStartname,"-",boneEndname)
    print(boneStart,boneEnd)
    print(f"""{boneLength:.3f}""")
    print()
    
    #---https://developer.valvesoftware.com/wiki/$jigglebone
    #---replace your jigglebone code here, keep {bone.name} so that the script 
    #---replaces it with every bone.
    #---pitch  = X rotation, positive rotation is the negative in blender
    #---yaw    = Y rotation, positive rotation is the negative in blender
    #---yes it's annoying like that.
    #---stiffness  [0:1000] low:loose and weak, high: stiff and springy
    #---damping    [0:1000] 0:oscillates forever, 1000 stops instantly
    #---multiply the length to get a "lower gravity effect"
    
    jiggle_creator = f"""$jigglebone {bone.name}
{{
    is_flexible
    {{
        length {boneLength*10:.3f}
        tip_mass 150
        along_stiffness 100
        along_damping 0
        angle_constraint 30
        pitch_constraint -10 30
        pitch_stiffness 100
        pitch_damping 20
        yaw_constraint -20 20
        yaw_stiffness 35
        yaw_damping 20
    }}
}}"""
    bloque_texto.write(jiggle_creator + "\n\n")
    
    #print(jiggle_creator)
    #carpeta_local = bpy.data.filepath
    
    #you can uncomment these 2 lines and replace the full filepath to be created
    #if you want to directly create the script instead of copypasting it.
    #with open("C:\\Users\\grogcito\\Desktop\\gangrena.qci","a") as file:
    #    file.write(jiggle_creator + "\n\n")
    

#stuff to create a new window. Unused because it always opens a new window
#and it leaks screen data.
'''
for ventana in bpy.data.screens.keys():
    indice = bpy.data.screens.keys().index(ventana)
    bpy.data.screens['temp'].user_clear()
nueva_ventana1 = bpy.ops.wm.window_new()
nueva_ventana = bpy.context.window_manager.windows[-1]

nueva_ventana.screen.areas[0].spaces.active.text = bloque_texto
bpy.ops.text.move(type='FILE_TOP')
bpy.ops.screen.delete()

#cleanup
contador = 
for ventana in bpy.data.screens.keys():
     print(bpy.data.screens[ventana].name)
     contador = contador + 1
     print(contador)
     conti = str(contador)
     if ventana == ('temp.00' + conti) : bpy.data.screens[ventana].user_clear()    
'''