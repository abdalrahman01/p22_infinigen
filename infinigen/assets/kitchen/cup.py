import bpy
from infinigen.core.placement.factory import AssetFactory
from infinigen.assets.utils import object
import numpy as np

class CupFactory(AssetFactory):
    body_dim_x = np.random.uniform(150, 90) # dimension in x 
    body_dim_y = np.random.uniform(150, 90) # dimension in y
    body_dim_z = np.random.uniform(90, 130) 
    handle_height = body_dim_x / 3.5
    handle_width = 10
    handle_depth = 5
    origin = (0,0,0)
    
    
    def __init__(self, seed):
        super(CupFactory, self).__init__(seed)

    def cup_handle(self) -> bpy.types.Object:
        handle_up_size = (self.handle_width, self.handle_depth,self.handle_depth)
        handle_down_size = handle_up_size
        handle_side_size = (self.handle_depth, self.handle_depth, self.handle_height)
        
        
        handle_up_loc = (0,0,self.handle_height - self.handle_depth)
        handle_side_loc = (self.handle_width/2, 0, self.handle_height/2 - self.handle_depth/2)
        
        handle_up = object.new_cube(location=handle_up_loc)
        handle_up.dimensions = handle_up_size
        handle_down = object.new_cube()
        handle_down.dimensions = handle_down_size
        handle_side = object.new_cube(location=handle_side_loc)
        handle_side.dimensions = handle_side_size
        
        bpy.ops.object.select_all(action='DESELECT')
        handle_up.select_set(True)
        handle_down.select_set(True)
        handle_side.select_set(True)
        bpy.ops.object.join()
        parent = bpy.context.active_object
        return parent
        
    def budy(self) -> bpy.types.Object:
        body_size = (self.body_dim_x, self.body_dim_y, self.body_dim_z)
        body_coo = self.origin
        body = object.new_cube(location=body_coo)
        body.dimensions = body_size
        return body
        
    def create_asset(self, **params) -> bpy.types.Object:
        body = self.budy()
       
        handle_parts = self.cup_handle()

        body.location = (-self.body_dim_x/2 - self.handle_width/2, 0, 0)
        bpy.ops.object.select_all(action='DESELECT')
        body.select_set(True)
        handle_parts.select_set(True)
        bpy.ops.object.join()
        parent =  bpy.context.active_object
        parent.location = (0, 0, 70)
        return parent