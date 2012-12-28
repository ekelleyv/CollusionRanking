# User class for simulation
import random

# possible votes
start = -2
downvote = -1
nothing = 0
upvote = 1

# possible groups a post or user can side with
no_group = 0
first_group = 1
second_group = 2

class User(object):
	def __init__(self, user_bias, id, num_posts):
		self.id = id                           # unique user id
		self.user_bias = user_bias             # is the user in a collusion
		self.voting_history = [start] * num_posts  # initialize a voting history array
		
	def vote(self, post):
		# if the user has not voted on this post
		if (self.voting_history[post.id] == -2):
			if (self.user_bias == 0):
				var = random.uniform(0, 1)
				# ignore 40% of the time
				if (var < 40):
					self.voting_history[post.id] = nothing
				# upvote 30% of the time
				elif (var < 70):
					self.voting_history[post.id] = upvote
					post.upvote()
				# downvote 30% of the time
				else:
					self.voting_history[post.id] = downvote
					post.downvote()
			else:
				# if biases are the same, with 99% probability upvote
				if (post.post_bias == self.user_bias and random.uniform(0, 1) < 0.99):
					self.voting_history[post.id] = upvote
					post.upvote()
				# else downvote with probability 65%, ignore 15%, upvote 20%
				else:
					var = random.uniform(0, 1)
					if (var < 65):
						self.voting_history[post.id] = downvote
						post.downvote()
					elif (var < 80):
						self.voting_history[post.id] = nothing
					else:
						self.voting_history[post.id] = upvote
						post.upvote()
				
				
				