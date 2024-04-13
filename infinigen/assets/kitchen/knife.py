import bpy
from infinigen.core.placement.factory import AssetFactory
from infinigen.assets.utils import object
import numpy as np
class KnifeFactory(AssetFactory):
    handle_length = np.random.uniform(100, 170)
    handle_width = np.random.uniform(10, 20)
    handle_thickness = 5
    blade_length = np.random.uniform(100, 200)
    blade_width = np.random.uniform(10, 20)
    blade_thickness = np.random.uniform(2, 4)
    origin = (0,0,0)
    
    def __init__(self, seed):
        super(KnifeFactory, self).__init__(seed)

    def create_asset(self, **params) -> bpy.types.Object:
        handle_size = (self.handle_length, self.handle_width, self.handle_thickness)
        handle_coo = self.origin
        blade_size = (self.blade_length, self.blade_width, self.blade_thickness)
        blade_coo = (handle_size[0]/2 + blade_size[0]/2 ,self.origin[1], self.origin[2])
        
        handle = object.new_cube(location=handle_coo)
        handle.dimensions = handle_size
        blade = object.new_cube(location=blade_coo)
        blade.dimensions = blade_size
        
        bpy.ops.object.select_all(action='DESELECT')
        handle.select_set(True)
        blade.select_set(True)
        bpy.ops.object.join()
        
        parent= bpy.context.active_object        
        return parent