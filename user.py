import random

class User(object):

	def __init__(self, user_type=0, num_stories=10):
		self.user_type = user_type
		self.voting_history = [0]*10

	def vote(self, story_type, story_index):
		voting_percentage = .9
		voting_bias = .9 #Chance they will vote for their side, for cliques only
		self.voting_history[story_index] = 0
		if (random.random() < voting_percentage):
			if (self.user_type == 0): #normal users
				if (random.randint(0, 1)):
					self.voting_history[story_index] = 1
				else:
					self.voting_history[story_index] = -1
			elif (self.user_type == story_type): #biased in favor
				if (random.random() < voting_bias):
					self.voting_history[story_index] = 1
				else:
					self.voting_history[story_index] = -1
			elif (self.user_type != story_type): #biased against
				if (random.random() > voting_bias):
					self.voting_history[story_index] = 1
				else:
					self.voting_history[story_index] = -1

	def print_votes(self):
		for i, vote in enumerate(self.voting_history):
			print "%d. %d" % (i, vote)

		