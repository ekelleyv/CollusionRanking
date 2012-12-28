# User class for simulation
import random

class User(object):
	def __init__(self, user_bias, id, num_posts):
		self.id = id                           # unique user id
		self.user_bias = user_bias             # is the user in a collusion
		self.voting_history = [-2] * num_posts  # initialize a voting history array
		
	def vote(self, post, post_id):
		y = 0
		# Add previous code
	
	def vote_block(self, time, post_array):
		# at most go back three hours (three hours * 60 minutes / hour * 3 posts / minute)
		last_hour = 60 * 3
		
		#if (random.uniform(0, 1) < 0.75):
		#	return
		
		# current number of posts 
		current_post_max_index = time
		
		# look at all current posts
		if (current_post_max_index < last_hour):
			for i in xrange(current_post_max_index):
				if (self.voting_history[i] == -2):
					self.vote(post_array[i], i)
		# look at last three hours
		else:
			for i in xrange(last_hour):
				if (self.voting_history[current_post_max_index - i] == -2):
					self.vote(post_array[current_post_max_index - i], current_post_max_index - i)