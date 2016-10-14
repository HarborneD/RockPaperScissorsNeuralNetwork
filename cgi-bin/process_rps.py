#!/usr/bin/python3

import cgi, cgitb
import json
from PyNet import NeuralNetwork
from rps_processor import RpsProcessor
import random 
import numpy as np

cgitb.enable() 


form = cgi.FieldStorage()

selection = form.getvalue("selection")
x_values = form.getvalue("x_values")

# guess_list = ["rock","paper","scissors"]

# guess = random.choice(guess_list)


NN = NeuralNetwork(weights_data_path="rps_weights.xml")

NN.set_input_data(np.matrix([float(i) for i in (x_values.split(","))]))

NN.run_net()

for i in range(0,NN.output_data[-1].shape[1]):
	if(i == 0):
		guess = "paper"
		largest = NN.output_data[-1].item(i)
	elif( NN.output_data[-1].item(i)> largest):
		if(i == 1):
			guess = "scissors"
			break
		else:
			guess = "rock"


proc = RpsProcessor(selection,x_values,guess)

proc.set_new_x()
proc.complete_fullset()



data={'correct':str(proc.result),'choice':guess,'x_values':proc.return_x_val_string(), 'fullset':proc.fullset}


print ('Content-Type: application/json\n\n')
print (json.dumps(data))

