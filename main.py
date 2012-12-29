# simulates multiple days of posts and users in a social content website
import random
import reddit

from user import User
from post import Post

# number of days in the simulation
num_days = 1

# number of users
num_users = 10000
num_posts = 4320

# possible groups a post or user can side with
no_group = 0
first_group = 1
second_group = 2

# probabilities of a post belonging to a collusive group
no_group_prob = .85
first_group_prob = .075
second_group_prob = .075

# probabilities of users belong to collusive groups
user_no_group_prob = .90
user_first_group_prob = .05
user_second_group_prob = .05

# textfile with all of the reports for each minute
textfile = file("SimulationReport.txt", "wt")

# print out a report of the last minute
def report(minute):
    textfile.write(str(minute / 30) + '\n')
	
# run  the simulation 
def main():
    # an array of posts and users
	content = [0] * num_posts
	users = []
	ranking = [0] * num_posts
    
    # ids of posts and users
	user_id = 0
	content_id = 0
    
	# initialize the number of users, create collusions
	for i in xrange(num_users):
        # determine user bias if any
		user_bias = -1
		user_bias_prob = random.uniform(0, 1)
		if (user_bias_prob < user_no_group_prob):
			user_bias = no_group
		elif (user_bias_prob < user_no_group_prob + user_first_group_prob):
			user_bias = first_group
		else:
			user_bias = second_group
        # create a new user
		users.append(User(user_bias = user_bias, id = user_id, num_posts = num_posts))
		user_id += 1
        
    # run simulation by the minute
	iterate = 60 * 24 * num_days
	for i in xrange(iterate):
        # create three new posts every minute
		number_new_posts = 3
        
		# number of new posts a minute
		for j in xrange(number_new_posts):
            # determine post bias if any for new post
			post_bias = -1
			post_bias_prob = random.uniform(0, 1)
			if (post_bias_prob < no_group_prob):
				post_bias = no_group
			elif (post_bias_prob < no_group_prob + first_group_prob):
				post_bias = first_group
			else:
				post_bias = second_group
			# create a new post
			content[content_id] = (Post(post_bias = post_bias, id = content_id, time = i))
			content_id += 1
    
        # go through all users and see if they will upvote/downvote posts
		for j in xrange(num_users):
			var = random.uniform(0, 1)
			if (var > 0.0):
				# look at the past hour
				last_hour = 60 * 3
				if (content_id < last_hour):
					for k in xrange(content_id):
						users[j].vote(post = content[k])
				else:
					for k in xrange(last_hour):
						w = content_id - k - 1
						users[j].vote(post = content[w])
    
		# call page rank algorithm for reddit
		if (i % 30 == 0 and not i == 0):
			print "------------------------------------------"
			for j in xrange(content_id - 1):
				if (content[j].post_bias == no_group):
					print str(reddit.hot(content[j].ups, content[j].downs, content[j].date))
				elif (content[j].post_bias == first_group):
					print "* " + str(reddit.hot(content[j].ups, content[j].downs, content[j].date))
				else:
					print "$ " + str(reddit.hot(content[j].ups, content[j].downs, content[j].date))
    
if __name__ == '__main__':
    main()