from user import User

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
			users.append(User(user_type=1, num_stories=num_stories))
		for j in range(bias_right):
			users.append(User(user_type=2, num_stories=num_stories))
		for j in range(unbiased):
			users.append(User(user_type=0, num_stories=num_stories))
		return users

	def initialize_stories(self, num_stories, percent_left=.1, percent_right=.1):
		stories = []
		bias_left = (int)(percent_left * num_stories)
		bias_right = (int)(percent_right * num_stories)
		unbiased = num_stories - (bias_left + bias_right)
		for j in range(bias_left):
			stories.append(1)
		for j in range(bias_right):
			stories.append(2)
		for j in range(unbiased):
			stories.append(0)
		return stories

	def hold_voting(self):
		for idx, val in enumerate(self.stories):
			for user in self.users:
				user.vote(story_type=val, story_index=idx)

	def print_stories(self):
		print "Printing stories"
		for i, story in enumerate(self.stories):
			print "%d. %d" % (i, story)

	def print_users(self):
		for i, user in enumerate(self.users):
			print "-----User %d------Type %d--------" % (i , user.user_type)
			user.print_votes()

if __name__ == '__main__':
	simulation = Simulation(10, 10)
	simulation.hold_voting()
	simulation.print_users()
