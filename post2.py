# class of posts for a social content website.  Posts can have bias.
import random
import datetime

class Post2(object):
	def __init__(self, post_bias, id, time, poster_id):
		self.post_bias = post_bias  # bias of the post
		self.id = id                # id of the post
		self.ups = 0				# number of upvotes
		self.downs = 0				# number of downvotes
		self.alt_ups = 0
		self.alt_downs = 0
		self.poster_id = poster_id

		hour = time / 60
		min = time % 60
		
		day = hour / 24 + 13
		hour = hour % 24
		
		date = datetime.datetime(2013, 1, day, hour, min)		
		self.date = date			# date of the post
		
	def upvote(self):
		self.alt_upvote()
		self.ups += 1

	def downvote(self):
		self.alt_downvote()
		self.downs += 1

	def alt_upvote(self):
		self.alt_ups += 1

	def alt_downvote(self):
		self.alt_downs += 1
