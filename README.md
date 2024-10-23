# Source-jigglebones-from-Bone-Collections
Generates $jigglebone code for every bone in a bone collection inside an armature
How to use:


  1. Select your armature, create a new bone collection, assign all the bones you want to that collection in pose mode.
  2. Select the Bone Collection, in the scripting workspace at the top load the script and run it.
  3. It will create a new text file inside blender called "Jiggles", you can select all with CTRL + A and copypaste it to your .qc file.
  4. The script won't work in edit mode, you must either be in object or pose mode with the armature selected.
  5. You can edit the script to your liking. I'd recommend increasing the 10 in "length {boneLength*10:.3f}" for "lower gravity" effect, or decreasing it for a higher grav effect
