
# simulates multiple days of posts and users in a social content website
import random
import detector
import time

from user2 import User2
from post2 import Post2

# number of days in the simulation
num_days = 1

# number of users
num_users = 100
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
#def report(minute):
    #textfile.write(str(minute / 30) + '\n')
    
# run  the simulation 
def main():
    # an array of posts and users
        content = [0] * num_posts
        users = []
        nb_users = []
        fg_users = []
        sg_users = []
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
                    # create a new user
                        nb_users.append(User2(user_bias = user_bias, id = user_id, num_posts = num_posts))
                        user_id += 1
                elif (user_bias_prob < user_no_group_prob + user_first_group_prob):
                        user_bias = first_group
                    # create a new user
                        fg_users.append(User2(user_bias = user_bias, id = user_id, num_posts = num_posts))
                        user_id += 1
                else:
                        user_bias = second_group
                    # create a new user
                        sg_users.append(User2(user_bias = user_bias, id = user_id, num_posts = num_posts))
                        user_id += 1
                        
                users.append(User2(user_bias = user_bias, id = user_id, num_posts = num_posts))
    
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
                    this_post_poster_id = -1
                    if (post_bias_prob < no_group_prob):
                        post_bias = no_group
                        this_post_poster_id = random.choice(nb_users).id
                    elif (post_bias_prob < no_group_prob + first_group_prob):
                        post_bias = first_group
                        this_post_poster_id = random.choice(fg_users).id
                    else:
                        post_bias = second_group
                        this_post_poster_id = random.choice(sg_users).id
                    # create a new post
                    content[content_id] = (Post2(post_bias = post_bias, id = content_id, time = i, poster_id = this_post_poster_id))
                    content_id += 1
    
        # go through all users and see if they will upvote/downvote posts
            for j in xrange(num_users):
                    var = random.uniform(0, 1)
                    
                    if (var > 0.0):
                        # look at the past hour
                        last_hour = 60 * 3
                        if (content_id < last_hour):
                                for k in xrange(content_id):
                                    users[j].vote(post = content[k],poster = users[content[k].poster_id])
                        else:
                                for k in xrange(last_hour):
                                    w = content_id - k - 1
                                    users[j].vote(post = content[w], poster = users[content[w].poster_id])



        # call page rank algorithm for reddit
        if (i % 30 == 0 and not i == 0):
                posts_ranking = []
                for j in xrange(content_id - 1):                        
                        post_data = [detector.hot(content[j].ups, content[j].downs, content[j].date), content[j].id]
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

        print '-------------------------------------'
        print '-----Detector------'
        print float(no_bias_sum3) / total
        print float(first_bias_sum3) / total
        print float(second_bias_sum3) / total
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    print time.time() - start_time



