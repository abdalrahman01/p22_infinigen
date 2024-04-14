import math

import bpy
import os
from infinigen.assets.kitchen import spoon, knife, fork, cup, dish
bpy.ops.object.select_all(action='SELECT')
bpy.context.scene.unit_settings.length_unit = "CENTIMETERS"
bpy.context.scene.unit_settings.scale_length = 0.001
bpy.ops.object.delete(use_global=False, confirm=False)

### 5 forks forming a pentagon and 5 spoons forming a pentagon, infront of it





# 5 forks forming a pentagon
def spawn_fork_pentagon():
    forkObjs = [fork.ForkFactory(0).spawn_asset(i) for i in range(5)]

    forkObjs[1].rotation_euler[1] = 1.5708
    forkObjs[2].rotation_euler[1] = 1.5708
    forkObjs[3].rotation_euler[1] = 0.942478
    forkObjs[4].rotation_euler[1] = 2.19911

    forkObjs[2].location[0] -= forkObjs[0].dimensions[0] 
    forkObjs[3].location[2] += forkObjs[1].dimensions[0] / 1.7
    forkObjs[4].location[0] -= forkObjs[0].dimensions[0] 
    forkObjs[4].location[2] += forkObjs[2].dimensions[0] / 1.7

    bpy.ops.object.select_all(action='DESELECT')
    
    for forkObj in forkObjs:
        forkObj.select_set(True)
        
    bpy.ops.object.join()
    
    return bpy.context.active_object


# 5 spoons forming a pentagon
def spawn_spoon_pentagon():
    spoonObjs = [spoon.SpoonFactory(0).spawn_asset(i) for i in range(5)]

    spoonObjs[1].rotation_euler[1] = 1.5708
    spoonObjs[2].rotation_euler[1] = 1.5708
    spoonObjs[3].rotation_euler[1] = 0.942478
    spoonObjs[4].rotation_euler[1] = 2.19911

    spoonObjs[2].location[0] -= spoonObjs[0].dimensions[0] 
    spoonObjs[3].location[2] += spoonObjs[1].dimensions[0]
    spoonObjs[4].location[0] -= spoonObjs[0].dimensions[0]
    spoonObjs[4].location[2] = spoonObjs[2].dimensions[0]
    
    bpy.ops.object.select_all(action='DESELECT')
    
    for spoonObj in spoonObjs:
        spoonObj.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object

# 5 knifes forming a pentagon
def spawn_knife_pentagon():
    knifeObjs = [knife.KnifeFactory(0).spawn_asset(i) for i in range(5)]

    knifeObjs[1].rotation_euler[1] = 1.5708
    knifeObjs[2].rotation_euler[1] = 1.5708
    knifeObjs[3].rotation_euler[1] = 0.942478
    knifeObjs[4].rotation_euler[1] = 2.19911

    knifeObjs[2].location[0] -= knifeObjs[0].dimensions[0] / 1.7
    knifeObjs[3].location[2] += knifeObjs[1].dimensions[0] / 1.7
    knifeObjs[4].location[0] -= knifeObjs[0].dimensions[0] / 1.7
    knifeObjs[4].location[2] += knifeObjs[2].dimensions[0] / 1.7

    bpy.ops.object.select_all(action='DESELECT')
    
    for knifeObj in knifeObjs:
        knifeObj.select_set(True)
        
    bpy.ops.object.join()
    
    return bpy.context.active_object
# 3 forks forming a triangle
def spawn_fork_triangle():
    forkObj1 = fork.ForkFactory(0).spawn_asset(0)
    forkObj2 = fork.ForkFactory(0).spawn_asset(1)
    forkObj3 = fork.ForkFactory(0).spawn_asset(2)

    forkObj3.location[0] -= forkObj1.dimensions[0] / 2
    forkObj3.location[2] += forkObj3.dimensions[0] / 2

    forkObj3.rotation_euler[1] -= 1.0472
    forkObj2.rotation_euler[1] += 1.0472

    bpy.ops.object.select_all(action='DESELECT')
    
    forkObj1.select_set(True)
    
    forkObj2.select_set(True)
    
    forkObj3.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object

# 3 spoons forming a triangle
def spawn_spoon_triangle():
    spoonObj1 = spoon.SpoonFactory(0).spawn_asset(0)
    spoonObj2 = spoon.SpoonFactory(0).spawn_asset(1)
    spoonObj3 = spoon.SpoonFactory(0).spawn_asset(2)

    spoonObj3.location[0] -= spoonObj1.dimensions[0] / 2
    spoonObj3.location[2] += spoonObj3.dimensions[0] / 2

    spoonObj3.rotation_euler[1] -= 1.0472
    spoonObj2.rotation_euler[1] += 1.0472

    bpy.ops.object.select_all(action='DESELECT')
    
    spoonObj1.select_set(True)
    spoonObj2.select_set(True)
    spoonObj3.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object

# 3 knifes forming a triangle
def spawn_knife_triangle():
    knifeObj1 = knife.KnifeFactory(0).spawn_asset(0)
    knifeObj2 = knife.KnifeFactory(0).spawn_asset(1)
    knifeObj3 = knife.KnifeFactory(0).spawn_asset(2)

    knifeObj3.location[0] -= knifeObj1.dimensions[0] / 2
    knifeObj3.location[2] += knifeObj3.dimensions[0] / 2

    knifeObj3.rotation_euler[1] -= 1.0472
    knifeObj2.rotation_euler[1] += 1.0472

    bpy.ops.object.select_all(action='DESELECT')
    
    knifeObj1.select_set(True)
    knifeObj2.select_set(True)
    knifeObj3.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object
# 4 spoons forming a square
def spawn_spoon_rec():
    spoonObj1 = spoon.SpoonFactory(0).spawn_asset(0)
    spoonObj2 = spoon.SpoonFactory(0).spawn_asset(1)
    spoonObj3 = spoon.SpoonFactory(0).spawn_asset(2)
    spoonObj4 = spoon.SpoonFactory(0).spawn_asset(3)

    spoonObj3.location[1] -= spoonObj2.dimensions[0] + 10
    spoonObj4.location[0] -= spoonObj2.dimensions[0] + 10

    spoonObj2.rotation_euler[2] = 1.5708
    spoonObj4.rotation_euler[2] = 1.5708
    
    bpy.ops.object.select_all(action='DESELECT')
    
    spoonObj1.select_set(True)
    spoonObj2.select_set(True)
    spoonObj3.select_set(True)
    spoonObj4.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object

# 4 knifes forming a square
def spawn_knife_rec():
    knifeObj1 = knife.KnifeFactory(0).spawn_asset(0)
    knifeObj2 = knife.KnifeFactory(0).spawn_asset(1)
    knifeObj3 = knife.KnifeFactory(0).spawn_asset(2)
    knifeObj4 = knife.KnifeFactory(0).spawn_asset(3)

    knifeObj3.location[1] -= knifeObj2.dimensions[0] + 10
    knifeObj4.location[0] -= knifeObj2.dimensions[0] + 10

    knifeObj2.rotation_euler[2] = 1.5708
    knifeObj4.rotation_euler[2] = 1.5708
    bpy.ops.object.select_all(action='DESELECT')
    
    knifeObj1.select_set(True)
    knifeObj2.select_set(True)
    knifeObj3.select_set(True)
    knifeObj4.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object
    

# 4 forks forming a square
def spawn_fork_rec():
    forkObj1 = fork.ForkFactory(0).spawn_asset(0)
    forkObj2 = fork.ForkFactory(0).spawn_asset(1)
    forkObj3 = fork.ForkFactory(0).spawn_asset(2)
    forkObj4 = fork.ForkFactory(0).spawn_asset(3)

    forkObj3.location[1] -= forkObj2.dimensions[0] + 10
    forkObj4.location[0] -= forkObj2.dimensions[0] + 10

    forkObj2.rotation_euler[2] = 1.5708
    forkObj4.rotation_euler[2] = 1.5708
    
    bpy.ops.object.select_all(action='DESELECT')
    
    forkObj1.select_set(True)
    forkObj2.select_set(True)
    forkObj3.select_set(True)
    forkObj4.select_set(True)
    
    bpy.ops.object.join()
    
    return bpy.context.active_object




cupObj = cup.CupFactory(0).spawn_asset(0)
forkObj = fork.ForkFactory(0).spawn_asset(1)
knifeObj = knife.KnifeFactory(0).spawn_asset(2)

# Position the fork to the left of the cup
forkObj.location[0] = cupObj.dimensions[0] / 2 + forkObj.dimensions[0] / 2 + 10

# Position the knife to the right of the cup
knifeObj.location[0] = -cupObj.dimensions[0] / 2 - knifeObj.dimensions[0] / 2 - 10

export_path = os.path.join(os.getcwd(), "cup_dish.gltf")
bpy.ops.export_scene.gltf(filepath=export_path)