#reddit algorithm + noise

from datetime import datetime, timedelta
from math import log
import random
import numpy

epoch = datetime(1970, 1, 1)
noise = .20

def epoch_seconds(date):
	#"""Returns the number of seconds from the epoch to date."""
	td = date - epoch
	return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def score(ups, downs):
	return ups - downs

def extend_up(upvoter, poster):
	for key in poster.upvote_tracker:
		update = 0
		if (poster.upvote_tracker[key] != 0):
			update = log(abs(poster.upvote_tracker[key]))

		if upvoter.upvote_tracker.has_key(key):
			oldcount = upvoter.upvote_tracker[key]
			upvoter.upvote_tracker[key] = oldcount + update
		else:
			upvoter.upvote_tracker[key] = update

	for key in poster.downvote_tracker:
		update = 0
		if (poster.downvote_tracker[key] != 0):
			update = log(abs(poster.downvote_tracker[key]))

		if upvoter.downvote_tracker.has_key(key):
			oldcount = upvoter.downvote_tracker[key]
			upvoter.downvote_tracker[key] = oldcount + update
		else:
			upvoter.downvote_tracker[key] = update
				
def extend_down(downvoter, poster):
	
	for key in poster.upvote_tracker:
		update = 0
		if (poster.upvote_tracker[key] != 0):
			update = log(abs(poster.upvote_tracker[key]))

		# print "Update %f" % update
		
		if downvoter.upvote_tracker.has_key(key):
			oldcount = downvoter.upvote_tracker[key]
			downvoter.upvote_tracker[key] = oldcount - update
		else:
			downvoter.upvote_tracker[key] = 0 - update

	for key in poster.downvote_tracker:
		update = 0
		if (poster.downvote_tracker[key] != 0):
			update = log(abs(poster.downvote_tracker[key]))

		if downvoter.downvote_tracker.has_key(key):
			oldcount = downvoter.downvote_tracker[key]
			downvoter.downvote_tracker[key] = oldcount - update
		else:
			downvoter.downvote_tracker[key] = 0 - update

def vote_decider_up(user, post):
	allups = float(sum(user.upvote_tracker.values()))
	std = numpy.std(user.upvote_tracker.values())
	mean = numpy.mean(user.upvote_tracker.values())
	# print user.upvote_tracker.values()
	# print "User %d, Allups : %f" % (user.id, allups)
	if user.upvote_tracker.has_key(post.poster_id) and allups > 50:
		if (user.upvote_tracker[post.poster_id] > mean + std):
			post.alt_downvote()

def vote_decider_down(user, post):
	alldowns = float(sum(user.downvote_tracker.values()))
	std = numpy.std(user.downvote_tracker.values())
	mean = numpy.mean(user.downvote_tracker.values())
	# print "User %d, Alldowns : %f" % (user.id, alldowns)
	if user.downvote_tracker.has_key(post.poster_id) and alldowns > 50:
		if (user.downvote_tracker[post.poster_id] > mean + std):
			post.alt_upvote()                  
					

def hot(ups, downs, date):
	#"""The hot formula. Should match the equivalent function in postgres."""
	s = score(ups, downs)
	order = log(max(abs(s), 1), 10)
	sign = 1 if s > 0 else -1 if s < 0 else 0
	seconds = epoch_seconds(date) - 1134028003
	return round(order + sign * seconds / 45000, 7)
