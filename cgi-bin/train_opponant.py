#!/usr/bin/python3

import cgi, cgitb

from PyNet import NeuralNetwork

cgitb.enable() 


NN = NeuralNetwork(training_data_path="result_data.csv",init_weight_config=[27,15,3])

NN.train_net(2000,save_name="rps_weights.xml")



print( 'Content-Type: text/html; charset=utf-8')
print( '')
print( '<!DOCTYPE html>')
print( '<html>')
print("Net Trained")
print( '</html>')
