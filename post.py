# class of posts for a social content website.  Posts can have bias.
import random
import datetime

class Post(object):
	def __init__(self, post_bias, id, time):
		self.post_bias = post_bias  # bias of the post
		self.id = id                # id of the post
		self.ups = 0				# number of upvotes
		self.downs = 0				# number of downvotes

		hour = time / 60
		min = time % 60
		date = datetime.datetime(2013, 1, 13, hour, min)		
		self.date = date			# date of the post
		
	def upvote(self):
		self.ups += 1

	def downvote(self):
		self.downs += 1