# User class for simulation
import random
import detector

# possible votes
start = -2
downvote = -1
nothing = 0
upvote = 1

# possible groups a post or user can side with
no_group = 0
first_group = 1
second_group = 2


class User2(object):
	def __init__(self, user_bias, id, num_posts):
		self.id = id                           # unique user id
		self.user_bias = user_bias             # is the user in a collusion
		self.voting_history = [start] * num_posts  # initialize a voting history array
		self.upvote_tracker = {}
		self.downvote_tracker = {}
		
	def vote(self, post, poster):
		# if the user has not voted on this post
		if (self.voting_history[post.id] == start):
			if (self.user_bias == 0):
				var = random.uniform(0, 1)
				# ignore 60% of the time
				if (var < 0.60):
					self.voting_history[post.id] = nothing
				# upvote 25% of the time
				elif (var < 0.85):
					self.voting_history[post.id] = upvote
					if (post.poster_id in self.upvote_tracker):
												old_count = self.upvote_tracker[post.poster_id]
												self.upvote_tracker[post.poster_id] = old_count + 1
										else:
												self.upvote_tracker[post.poster_id] = 1
					post.upvote()
					detector.extend_up(self, poster)
					detector.vote_decider_up(self, post)
					
				# downvote 15% of the time
				else:
					self.voting_history[post.id] = downvote
					if (post.poster_id in self.upvote_tracker):
												old_count = self.downvote_tracker[post.poster_id]
												self.downvote_tracker[post.poster_id] = old_count + 1
										else:
												self.downvote_tracker[post.poster_id] = +1
					post.downvote()
					detector.extend_down(self, poster)
					detector.vote_decider_down(self, post)
					
			else:
				# if biases are the same, with 99% probability upvote
				if (post.post_bias == self.user_bias and random.uniform(0, 1) < 0.99):
					self.voting_history[post.id] = upvote
					if (post.poster_id in self.upvote_tracker):
												old_count = upvote_tracker[post.poster_id]
												self.upvote_tracker[post.poster_id] = old_count + 1
										else:
												self.upvote_tracker[post.poster_id] = 1
					post.upvote()
					detector.extend_up(self, poster)
					detector.vote_decider_up(self, post)
				# else downvote with probability 40%, ignore 40%, upvote 20%
				else:
					var = random.uniform(0, 1)
					if (var < 0.40):
						self.voting_history[post.id] = downvote
												if (post.poster_id in self.upvote_tracker):
														print self.downvote_tracker
														old_count = self.downvote_tracker[post.poster_id]
														self.downvote_tracker[post.poster_id] = old_count + 1
												else:
														self.downvote_tracker[post.poster_id] = +1
												post.downvote()
												detector.extend_down(self, poster)
												detector.vote_decider_down(self, post)
														
					elif (var < 0.80):
						self.voting_history[post.id] = nothing
					else:
						self.voting_history[post.id] = upvote
						if (post.poster_id in self.upvote_tracker):
														old_count = upvote_tracker[post.poster_id]
														self.upvote_tracker[post.poster_id] = old_count + 1
												else:
														self.upvote_tracker[post.poster_id] = 1
						post.upvote()
						detector.extend_up(self, poster)
						detector.vote_decider_up(self, post)


