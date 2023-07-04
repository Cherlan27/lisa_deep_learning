# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:34:50 2023

@author: petersdorf
"""

from mlreflect.data_generation import Layer, Substrate, AmbientLayer, MultilayerStructure

class structure_creater():
    def __init__(self, number_layer, thickness, roughness, sld, thickness1, roughness1, sld1, thickness2, roughness2, sld2):
        self.thickness = thickness
        self.roughness = roughness
        self.sld = sld      
        
        self.thickness_layer = [thickness1, thickness2]
        self.roughness_layer = [roughness1, roughness2]
        self.sld_layer = [sld1,sld2]
        
        self.substrate = Substrate('H2O', self.roughness, self.sld) 
        self.ambient = AmbientLayer('ambient', 0)
        self.sample = MultilayerStructure()
        self.sample.set_substrate(self.substrate)
        self.sample.set_ambient_layer(self.ambient)
        self.add_layering(number_layer)
    
    def add_layering(self, number_layer):
        for i in range(number_layer):
            str_name = "Layer" + str(i)
            layer_gen = Layer(str_name, self.thickness_layer[i], self.roughness_layer[i], self.sld_layer[i])
            self.sample.add_layer(layer_gen)
        
    def get_sample(self):
        return self.sample
        