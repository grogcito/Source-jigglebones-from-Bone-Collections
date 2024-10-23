# Source-jigglebones-from-Bone-Collections
Generates $jigglebone code for every bone in a bone collection inside an armature
How to use:


  1. download the script and load it in blender text editor
  2. Select your armature, create a new bone collection, assign all the bones you want to that collection in pose mode.
  3. Run the script
  4. It will create a new text file inside blender called "Jiggles", with all the bones from your active selection
  5. The script won't work in edit mode, you must either be in object or pose mode with the armature selected.
  6. You can edit the script to your liking. I'd recommend changing the 10 in "length {boneLength*10:.3f}", a higher number gets you a "low gravity" effect and vice versa
