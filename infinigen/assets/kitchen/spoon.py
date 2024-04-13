import bpy
from infinigen.core.placement.factory import AssetFactory
from infinigen.assets.utils import object
import numpy as np
class SpoonFactory(AssetFactory):
    handle_length = np.random.uniform(100, 170)
    handle_width = np.random.uniform(10, 15)
    handle_thickness = np.random.uniform(2, 4)
    bowl_length = np.random.uniform(20, 40)
    bowl_width = np.random.uniform(15, 20)
    bowl_depth = np.random.uniform(10, 20)
    bowl_thickness = np.random.uniform(2, 4)
    origin = (0,0,0)
    
    def __init__(self, seed):
        super(SpoonFactory, self).__init__(seed)
        
    def create_bowl(self):
        bottem_location = (self.origin[0] + self.handle_length / 2 + self.bowl_length/2, 0,-self.bowl_depth/2-self.bowl_thickness/2)
        
        
        south_wall_location = (self.origin[0] + self.handle_length / 2 + self.bowl_thickness/2, self.origin[1], self.origin[2])
        
        north_wall_location = (self.origin[0] + self.handle_length / 2 - self.bowl_thickness/2+  self.bowl_length, self.origin[1],self.origin[2])
        
        east_wall_location = (self.origin[0] + self.handle_length / 2 + self.bowl_length/2, -self.bowl_width/2, 0)
        west_wall_location = (self.origin[0] + self.handle_length / 2 + self.bowl_length/2, self.bowl_width/2, 0)
        
        swall = object.new_cube(location=south_wall_location)
        swall.dimensions = (self.bowl_thickness,self.bowl_width, self.bowl_depth)
        
        nwall = object.new_cube(location=north_wall_location)
        nwall.dimensions = (self.bowl_thickness,self.bowl_width, self.bowl_depth)
        
        ewall = object.new_cube(location=east_wall_location)
        ewall.dimensions = (self.bowl_length, self.bowl_thickness, self.bowl_depth)
        
        wwall = object.new_cube(location=west_wall_location)
        wwall.dimensions = (self.bowl_length, self.bowl_thickness, self.bowl_depth)
        
        bottem = object.new_cube(location=bottem_location)
        bottem.dimensions = (self.bowl_length, self.bowl_width, self.bowl_thickness)
        
        bpy.ops.object.select_all(action='DESELECT')
        swall.select_set(True)
        nwall.select_set(True)
        ewall.select_set(True)
        wwall.select_set(True)
        bottem.select_set(True)
        bpy.ops.object.join()
        
        return bpy.context.active_object
        
        
    def create_asset(self, **params) -> bpy.types.Object:
        handle_location = self.origin
        handle_dim = (self.handle_length, self.handle_width, self.handle_thickness)
        handle = object.new_cube(location=handle_location)
        handle.dimensions = handle_dim
        bowl = self.create_bowl()
        
        bpy.ops.object.select_all(action='DESELECT')
        handle.select_set(True)
        bowl.select_set(True)
        bpy.ops.object.join()
        parent= bpy.context.active_object
        return parent        
    