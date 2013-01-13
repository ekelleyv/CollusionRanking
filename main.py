# simulates multiple days of posts and users in a social content website
import random
import sampling
import time
import reddit
import noisy

from user import User
from post import Post

# number of days in the simulation
num_days = 1

# number of users
num_users = 1000
num_posts = 4320

# possible groups a post or user can side with
no_group = 0
first_group = 1
second_group = 2

# probabilities of a post belonging to a collusive group
no_group_prob = .96
first_group_prob = .02
second_group_prob = .02

# probabilities of users belong to collusive groups
user_no_group_prob = .95
user_first_group_prob = .025
user_second_group_prob = .025

# textfile with all of the reports for each minute
textfile = file("SimulationReport.txt", "wt")

# print out a report of the last minute
#def report(minute):
#    textfile.write(str(minute / 30) + '\n')
	
# run  the simulation 
def main():
	for q in xrange(0, 50):
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
			
		no_bias_sum = 0
		first_bias_sum = 0
		second_bias_sum = 0
			
		no_bias_sum2 = 0
		first_bias_sum2 = 0
		second_bias_sum2 = 0		
		
		no_bias_sum3 = 0
		first_bias_sum3 = 0
		second_bias_sum3 = 0	
		
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
				posts_ranking = []
				for j in xrange(content_id - 1):	
					post_data = [reddit.hot(content[j].ups, content[j].downs, content[j].date), content[j].id]
					posts_ranking.append(post_data)
					
				sorted_by_second = sorted(posts_ranking, key=lambda tup: tup[0], reverse = True)
				
				no_bias_number = 0
				first_bias_number = 0
				second_bias_number = 0
				
				for b in xrange(0, 30):
					id = sorted_by_second[b][1]
					if (content[id].post_bias == no_group):
						no_bias_number += 1
					elif (content[id].post_bias == first_group):
						first_bias_number += 1
					else:
						second_bias_number += 1
				no_bias_sum += no_bias_number
				first_bias_sum += first_bias_number
				second_bias_sum += second_bias_number
				
				posts_ranking = []
				for j in xrange(content_id - 1):	
					post_data = [sampling.hot(content[j].ups, content[j].downs, content[j].date), content[j].id]
					posts_ranking.append(post_data)
					
				sorted_by_second = sorted(posts_ranking, key=lambda tup: tup[0], reverse = True)
				
				no_bias_number = 0
				first_bias_number = 0
				second_bias_number = 0
				
				for b in xrange(0, 30):
					id = sorted_by_second[b][1]
					if (content[id].post_bias == no_group):
						no_bias_number += 1
					elif (content[id].post_bias == first_group):
						first_bias_number += 1
					else:
						second_bias_number += 1
				no_bias_sum2 += no_bias_number
				first_bias_sum2 += first_bias_number
				second_bias_sum2 += second_bias_number
				
				posts_ranking = []
				for j in xrange(content_id - 1):	
					post_data = [noisy.hot(content[j].ups, content[j].downs, content[j].date), content[j].id]
					posts_ranking.append(post_data)
					
				sorted_by_second = sorted(posts_ranking, key=lambda tup: tup[0], reverse = True)
				
				no_bias_number = 0
				first_bias_number = 0
				second_bias_number = 0
				
				for b in xrange(0, 30):
					id = sorted_by_second[b][1]
					if (content[id].post_bias == no_group):
						no_bias_number += 1
					elif (content[id].post_bias == first_group):
						first_bias_number += 1
					else:
						second_bias_number += 1
				no_bias_sum3 += no_bias_number
				first_bias_sum3 += first_bias_number
				second_bias_sum3 += second_bias_number
				
		total = no_bias_sum + first_bias_sum + second_bias_sum
		print '-----Reddit-----'
		print float(no_bias_sum) / total
		print float(first_bias_sum) / total
		print float(second_bias_sum) / total
		print '----Sampling----'
		print float(no_bias_sum2) / total
		print float(first_bias_sum2) / total
		print float(second_bias_sum2) / total
		print '-----Noisy------'
		print float(no_bias_sum3) / total
		print float(first_bias_sum3) / total
		print float(second_bias_sum3) / total
	
if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time() - start_time
