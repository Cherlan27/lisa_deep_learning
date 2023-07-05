# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:36:58 2023

@author: petersdorf
"""

from training_water import water_training

train_h2o = water_training(2, (0, 12), (1.5,3.9), (0, 12), (0, 18), (1,3.9), (0, 12), (0, 25), (1,3.9), (0, 12))
train_h2o.print_structure()
train_h2o.training_generator(2**19)
train_h2o.get_loss(70)
train_h2o.fit_model()
train_h2o.get_prediction_tests()

train_h2o.saving_model("trained_2_02_layer.h5")