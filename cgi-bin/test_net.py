from PyNet import NeuralNetwork
import numpy as np

x_list = (["0"]*27)
x_list[0] = "1"
x_values = ",".join(x_list)
x_values="0.0,1,0.0,0.0,0.0,1,0.0,0.0,1,1,1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.4444444444444444,0.4444444444444444,0.1111111111111111,9.0,2.0"



NN = NeuralNetwork(weights_data_path="rps_weights.xml")

NN.set_input_data(np.matrix([float(i) for i in (x_values.split(","))]))

NN.run_net()

print(NN.output_data)

for i in range(0,NN.output_data[-1].shape[1]):
	if(i == 0):
		guess = "rock"
		largest = NN.output_data[-1].item(i)
	elif( NN.output_data[-1].item(i)> largest):
		if(i == 1):
			guess = "paper"
			break
		else:
			guess = "scissors"

print(guess)