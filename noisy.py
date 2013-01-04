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
    new_ups = 0
    new_downs = 0
    for x in range(0, ups):
            noise_prob = random.uniform(0,1)
            if (noise_prob < noise):
                    new_downs += 1
            else:
                    new_ups += 1

    for y in range(0, downs):
            noise_prob = random.uniform(0,1)
            if (noise_prob < noise):
                    new_ups += 1
            else:
                    new_downs += 1
                    
    return new_ups - new_downs

def hot(ups, downs, date):
    #"""The hot formula. Should match the equivalent function in postgres."""
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)
