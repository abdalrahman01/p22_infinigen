import bpy
from infinigen.core.placement.factory import AssetFactory
from infinigen.assets.utils import object
import numpy as np

class ForkFactory(AssetFactory):
    handle_length = np.random.uniform(100, 170)
    handle_width = np.random.uniform(10, 20)
    handle_thickness = 5
    tine_length = np.random.uniform(20, 40)
    tine_width = np.random.uniform(3, 5)
    tine_thickness = np.random.uniform(2, 4)
    tine_count = np.random.randint(3, 6)
    # tine_count = 6
    
    tine_base_length = tine_width * tine_count + 10
    origin = (0,0,0)
    
    def __init__(self, seed):
        super(ForkFactory, self).__init__(seed)

    def create_asset(self, **params) -> bpy.types.Object:
        handle_size = (self.handle_length, self.handle_width, self.handle_thickness)
        handle_coo = self.origin
        tine_base_size = (3, self.tine_base_length, handle_size[2]+2)
        
        tine_base_coo = (handle_size[0]/2 + tine_base_size[0]/2 ,self.origin[1], self.origin[2])
        tines_size = (30, 3, tine_base_size[2]) 
        tines_coo = [(tine_base_coo[0]+ tines_size[0]/2, tine_base_size[1]/2, self.origin[2]), 
                     (tine_base_coo[0] + tines_size[0]/2, -tine_base_size[1]/2, self.origin[2]),
                     (tine_base_coo[0]+ tines_size[0]/2, self.origin[1], self.origin[2])]
        handle = object.new_cube(location=handle_coo)
        handle.dimensions = handle_size
        tine_base = object.new_cube(location=tine_base_coo)
        tine_base.dimensions = tine_base_size
        
        tines = []
        for i in range(self.tine_count):
            obj = object.new_cube(location=(tine_base_coo[0]+ tines_size[0]/2, self.get_y_pos_for_tine(i,tine_count=self.tine_count), self.origin[2]))
            tines.append(obj)
            tines[i].dimensions = tines_size
        
        # tines = [object.new_cube(location=c, scale=tines_size) for c in tines_coo]
        bpy.ops.object.select_all(action='DESELECT')
        handle.select_set(True)
        tine_base.select_set(True)
        for t in tines:
            t.select_set(True)
        bpy.ops.object.join()
        
        parent= bpy.context.active_object
        
        return parent
    
    def get_y_pos_for_tine(self, index, tine_count):
        # space envenly the tines
        
        if index == 0:
            return self.origin[1] + self.tine_base_length/2 - self.tine_width/2
        elif index == tine_count - 1:
            return self.origin[1] - self.tine_base_length/2 + self.tine_width/2
        
        
        if tine_count % 2 == 0:
            # If the number of tines is even, space them evenly around the origin
            return self.origin[1] + (index - tine_count / 2 + 0.05) * self.tine_width
        else:
            # If the number of tines is odd, place the middle one at the origin
            return self.origin[1] + (index - tine_count // 2) * self.tine_width
            
        