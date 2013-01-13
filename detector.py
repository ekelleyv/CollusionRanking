#reddit algorithm + noise

from datetime import datetime, timedelta
from math import log
import random

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
            if upvoter.upvote_tracker.has_key(key):
                    oldcount = upvoter.upvote_tracker[key]
                    upvoter.upvote_tracker[key] = oldcount + poster.upvote_tracker[key]
            else:
                    upvoter.upvote_tracker[key] = poster.upvote_tracker[key]

    for key in poster.downvote_tracker:
            if upvoter.downvote_tracker.has_key(key):
                    oldcount = upvoter.downvote_tracker[key]
                    upvoter.downvote_tracker[key] = oldcount + poster.downvote_tracker[key]
            else:
                    upvoter.downvote_tracker[key] = poster.downvote_tracker[key]
                
def extend_down(downvoter, poster):
    for key in poster.upvote_tracker:
            if downvoter.upvote_tracker.has_key(key):
                    oldcount = downvoter.upvote_tracker[key]
                    downvoter.upvote_tracker[key] = oldcount - poster.upvote_tracker[key]
            else:
                    downvoter.upvote_tracker[key] = 0 - poster.upvote_tracker[key]

    for key in poster.downvote_tracker:
            if downvoter.downvote_tracker.has_key(key):
                    oldcount = downvoter.downvote_tracker[key]
                    downvoter.downvote_tracker[key] = oldcount - poster.downvote_tracker[key]
            else:
                    downvoter.downvote_tracker[key] = 0 - poster.downvote_tracker[key]

def vote_decider_up(user, post):
    allups = float(sum(user.upvote_tracker.values()))
    if user.upvote_tracker.has_key(post.poster_id):
            if (user.upvote_tracker[post.poster_id] / allups > .1) and allups > 50:
                    post.downvote()

def vote_decider_down(user, post):
    alldowns = float(sum(user.downvote_tracker.values()))
    if user.downvote_tracker.has_key(post.poster_id):
            if (user.downvote_tracker[post.poster_id] / alldowns > .1) and alldowns > 50:
                    post.upvote()                  
                    

def hot(ups, downs, date):
    #"""The hot formula. Should match the equivalent function in postgres."""
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)
