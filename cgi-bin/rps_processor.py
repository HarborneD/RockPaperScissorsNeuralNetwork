
class RpsProcessor:
	def __init__(self,selection,x_values,guess):
		self.Prev_x = [ float(x) for x in x_values.split(",")]

		self.selection = selection

		self.guess = guess

		self.new_x = [0.0] * len(self.Prev_x)

		self.result = self.calculate_result(self.selection,self.guess)

		self.fullset = x_values+",||,"

	def calculate_result(self,player_move,opponant_move):

		if(player_move == opponant_move):
			return 0
		else:
			if(player_move == "paper"):
				if(opponant_move == "scissors"):
					return -1
				else:
					return 1

			if(player_move == "rock"):
				if(opponant_move == "paper"):
					return -1
				else:
					return 1

			if(player_move == "scissors"):
				if(opponant_move == "rock"):
					return -1
				else:
					return 1


	def set_last_move(self):
		if(self.selection == "rock"):
			self.new_x[0] =1
		
		if(self.selection == "paper"):
			self.new_x[1] =1
		
		if(self.selection == "scissors"):
			self.new_x[2] =1
		
	def set_last_guess(self):
		if(self.guess == "rock"):
			self.new_x[3] =1
		
		if(self.guess == "paper"):
			self.new_x[4] =1
		
		if(self.guess == "scissors"):
			self.new_x[5] = 1
		
	def set_win_and_tie(self):

		if(self.result == 1):
			self.new_x[6] = 1

		elif(self.result == 0):
			self.new_x[7] = 1

	def update_sequential_identical_moves_track(self):

		if(sum([(self.Prev_x[0]*self.new_x[0]),(self.Prev_x[1]*self.new_x[1]),(self.Prev_x[2]*self.new_x[2])])==0):
			self.new_x[8] = 1
		else:
			self.new_x[8] = 1 +self.Prev_x[8]

		if(self.new_x[8] > self.new_x[9]):
			self.new_x[9] = self.new_x[8]


	def update_history_track(self):


		self.new_x[10] = self.Prev_x[0]
		self.new_x[11] = self.Prev_x[1]
		self.new_x[12] = self.Prev_x[2]

		for i in range(10,13):
			self.new_x[i+3] = self.Prev_x[i]
			self.new_x[i+6] = self.Prev_x[i+3]
			self.new_x[i+9] = self.Prev_x[i+6]

	def update_ratios(self):

		self.new_x[25] = self.Prev_x[25] + 1 

		self.new_x[26] = self.Prev_x[26] + max(0,self.result)

		for i in range(0,3):
			old_number = round(self.Prev_x[25]*self.Prev_x[22 + i])
			self.new_x[22+i] = (old_number + self.new_x[i]) /  self.new_x[25]

	def set_new_x(self):

		self.set_last_move()
		self.set_last_guess()
		self.set_win_and_tie()
		self.update_sequential_identical_moves_track()
		self.update_history_track()
		self.update_ratios()

	def return_x_val_string(self):

		return ",".join([str(x) for x in self.new_x])

	def complete_fullset(self):
		for i in range(0,3):
			if(i > 0):
				self.fullset += ","
			self.fullset += str(self.new_x[i])

