import bpy
from infinigen.core.placement.factory import AssetFactory
from infinigen.assets.utils import object
import numpy as np

class DishFactory(AssetFactory):
    dim_z = np.random.uniform(5, 10) 
    dim_y = np.random.uniform(450, 520)
    dim_x = np.random.uniform(400, 500)
    rim_height = 5
    rim_dim_y = dim_y + 10
    rim_dim_x = dim_x + 10
    origin = (0,0,0)
    
    def __init__(self, seed):
        super(DishFactory, self).__init__(seed)

    def create_asset(self, **params) -> bpy.types.Object:
        base_size = (self.dim_x, self.dim_y, self.dim_z)
        base_coo = self.origin
        rim_size = (self.rim_dim_x, self.rim_dim_y, self.rim_height)
        rim_coo = (self.origin[0], self.origin[1], -(self.dim_z + self.rim_height)/2)
        
        base = object.new_cube(location=base_coo)
        base.dimensions = base_size
        rim = object.new_cube(location=rim_coo)
        rim.dimensions = rim_size
        
        bpy.ops.object.select_all(action='DESELECT')
        base.select_set(True)
        rim.select_set(True)
        bpy.ops.object.join()
        
        parent= bpy.context.active_object
        
        return parent