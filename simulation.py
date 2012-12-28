from user import *

class Simulation(object):

	def __init__(self, num_users, num_stories):
		self.users = self.initialize_users(num_users=num_users, num_stories=num_stories)
		self.stories = self.initialize_stories(num_stories=num_stories)

	def initialize_users(self, num_users, num_stories, percent_left=.1, percent_right=.1):
		users = []
		bias_left = (int)(percent_left * num_users)
		bias_right = (int)(percent_right * num_users)
		unbiased = num_users - (bias_left + bias_right)
		for j in range(bias_left):
			users.append(User(user_type=LEFT, num_stories=num_stories))
		for j in range(bias_right):
			users.append(User(user_type=RIGHT, num_stories=num_stories))
		for j in range(unbiased):
			users.append(User(user_type=NORMAL, num_stories=num_stories))
		return users

	def initialize_stories(self, num_stories, percent_left=.1, percent_right=.1):
		stories = []
		bias_left = (int)(percent_left * num_stories)
		bias_right = (int)(percent_right * num_stories)
		unbiased = num_stories - (bias_left + bias_right)
		for j in range(bias_left):
			stories.append(LEFT)
		for j in range(bias_right):
			stories.append(RIGHT)
		for j in range(unbiased):
			stories.append(NORMAL)
		return stories

	def hold_voting(self):
		for idx, val in enumerate(self.stories):
			print("Story #%d" % idx)
			for user in self.users:
				user.vote(story_type=val, story_index=idx)

	def print_stories(self):
		print "Printing stories"
		for i, story in enumerate(self.stories):
			print "%d. %d" % (i, story)

	def print_users(self):
		for i, user in enumerate(self.users):
			print "-----User %d------Type %s--------" % (i , self.get_user_type(user.user_type))
			user.print_votes()

	def get_user_type(self, obj_type):
		if (obj_type == NORMAL):
			return "Normal"
		elif (obj_type == LEFT):
			return "Left"
		else:
			return "Right"

if __name__ == '__main__':
	simulation = Simulation(num_users=10000, num_stories=1000)
	simulation.hold_voting()
	simulation.print_users()
