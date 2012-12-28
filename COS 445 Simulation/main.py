# simulates multiple days of posts and users in a social content website
import random

from user import User
from post import Post

# number of days in the simulation
num_days = 2

# number of users
num_users = 10000

# possible positions a post or user can take
#no_lean = 0
left_lean = 1
right_lean = 2

# probabilities of left, right, and none on posts
#no_lean_prob = ?
left_lean_prob = 0.90
right_lean_prob = 0.1

# probabilities of left, right, and none on users
#user_no_lean_prob = ?
user_left_lean_prob = 0.95
user_right_lean_prob = 0.05

# textfile with all of the reports for each minute
textfile = file("SimulationReport.txt", "wt")

# print out a report of the last minute
def report(minute):
    textfile.write(str(minute))

# run  the simulation 
def main():
    # an array of posts
    content = []
    users = []
    
    # ids of posts and users
    user_id = 0
    content_id = 0
    
    # initialize the number of users, create collusions
    for i in xrange(num_users):
        user_bias_prob = random.uniform(0, 1)
        user_bias = -1
        if (user_bias_prob < user_left_lean_prob):
            user_bias = left_lean
        #elif (user_bias_prob < user_no_lean_prob + user_left_lean_prob):
        #    user_bias = leaf_lean
        else:
            user_bias = right_lean
        users.append(User(user_bias = user_bias))
        
    # run simulation by the minute
    iterate = 60 * 24 * num_days
    for i in xrange(iterate):
        # create a variable number of posts for each minute
        number_new_posts = random.randint(0, 5)
        
        # number of new posts a minute
        for j in xrange(number_new_posts):
            # determine post bias if any for new post
            post_bias_prob = random.uniform(0, 1)
            post_bias = -1
            if (post_bias_prob < left_lean_prob):
                post_bias = left_lean
            #elif (post_bias_prob < no_lean_prob + left_lean_prob):
            #    post_bias = left_lean
            else:
                post_bias = right_lean
                
            content.append(Post(post_bias = post_bias, id = content_id, time = i))
            content_id += 1
            
        # have people vote on posts
        for j in xrange(num_users):
            # no user votes every minute
            
            users[j].vote_block()
        
        # call current reddit page rank algorithm
        
        # call our new page rank algorithm
        
        report(i)
    
if __name__ == '__main__':
    main()