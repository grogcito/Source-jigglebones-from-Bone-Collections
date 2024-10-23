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

for bone in coleccionHuesos.bones:
    n = coleccionHuesos.bones.keys().index(bone.name)
    LastBoneInCollection = n == len(coleccionHuesos.bones) - 1
    boneHasChildren = coleccionHuesos.bones[n].children.keys()
    boneStart = coleccionHuesos.bones[n].head_local

    if boneHasChildren:
        if LastBoneInCollection:
            boneEnd   = coleccionHuesos.bones[n].head_local
            boneLength = (boneStart - boneEnd).length
        else:
            boneEnd   = coleccionHuesos.bones[n+1].head_local
            boneLength = (boneStart - boneEnd).length   
    #---https://developer.valvesoftware.com/wiki/$jigglebone
    #---replace your jigglebone code here, keep {bone.name} so that the script 
    #---replaces it with every bone.
    #---pitch  = X rotation, positive rotation is the negative in blender
    #---yaw    = Y rotation, positive rotation is the negative in blender
    #---yes it's annoying like that.
    #---stiffness  [0:1000] low:loose and weak, high: stiff and springy
    #---damping    [0:1000] 0:oscillates forever, 1000 stops instantly
    #---Increasing the boneLength*X multiplier gives a low gravity effect.
    
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
    
    #you can uncomment these 2 lines and replace the full filepath to be created
    #if you want to directly create the script instead of copypasting it.
    #with open("C:\\Users\\grogcito\\Desktop\\gangrena.qci","a") as file:
    #    file.write(jiggle_creator + "\n\n")
