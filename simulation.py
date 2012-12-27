import User

class Simulation(object):

	def __init__(self, num_users, num_stories):
		self.users = self.initialize_users(num_users=num_users)
		self.stories = self.initialize_stories(num_stories=num_stories)

	def initialize_users(self, num_users, percent_left=.1, percent_right=.1):
		for i in range(num_users):
			bias_left = (int)(percent_left * num_users)
			bias_right = (int)(percent_right * num_users)
			unbiased = num_users - (bias_left + bias_right)
			for j in range(bias_left):
				self.users.append(User(user_type=1))
			for j in range(bias_right):
				self.user.append(User(user_type=2))
			for j in range(unbiased):
				self.user.append(User(user_type=0))

	def initialize_votes(self, num_stories, percent_left=.1, percent_right=.1):
		for i in range(num_stories):
			bias_left = (int)(percent_left * num_users)
			bias_right = (int)(percent_right * num_users)
			unbiased = num_users - (bias_left + bias_right)
			for j in range(bias_left):
				self.stories.append(1)
			for j in range(bias_right):
				self.stories.append(2)
			for j in range(unbiased):
				self.stories.append(0)

	def hold_voting(self):
		for i, story in self.stories:
			for j, user in self.users:
				user.vote(story_type=self.stories[i], story_index=i)

	def print_users(self):
		for i, user in self.users:
			print "-----User %d------Type %d--------"
			user.print_votes()

if __name__ == '__main__':
	simulation = Simulation(10, 10)
	simulation.hold_voting()
	simulation.print_users()
