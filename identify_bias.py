from user import User
from math import *
import random


#Clustering implementation from:
#http://stackoverflow.com/questions/1233593/k-means-clustering-implementation-in-python-running-out-of-memory
def simple_pearson(v1,v2):

    si = [val for val in v1 if val in v2]

    n = len(si)

    if n==0: return 0.0

    sum1 = 0.0
    sum2 = 0.0
    sum1_sq = 0.0
    sum2_sq = 0.0
    p_sum = 0.0

    for v in si:
        sum1+=v1[v]
        sum2+=v2[v]
        sum1_sq+=pow(v1[v],2)
        sum2_sq+=pow(v2[v],2)
        p_sum+=(v1[v]*v2[v])

    # Calculate Pearson score
    num = p_sum-(sum1*sum2/n)
    temp = (sum1_sq-pow(sum1,2)/n) * (sum2_sq-pow(sum2,2)/n)
    if temp < 0.0:
        temp = -temp
    den = sqrt(temp)
    if den==0: return 1.0

    r = num/den

    return r

def distance(v1,v2):
    return 1.0-simple_pearson(v1,v2)

def kcluster(prefs,k=21,max_iterations=50):
    from collections import defaultdict

    users = prefs.keys()
    centroids = [prefs[u] for u in random.sample(users, k)]

    print "Centroids are "
    print len(centroids)

    lastmatches = None
    for t in range(max_iterations):
        print 'Iteration %d' % t
        bestmatches = [[] for i in range(k)]

        # Find which centroid is closest for each row        
        for j in users:
            row = prefs[j]
            bestmatch=(0,2.0)

            for i in range(k):
                d = distance(row,centroids[i])
                if d <= bestmatch[1]: bestmatch = (i,d)
            bestmatches[bestmatch[0]].append(j)

        # If the results are the same as last time, this is complete
        if bestmatches == lastmatches: break
        lastmatches=bestmatches

        centroids = [defaultdict(float) for i in range(k)]

        #  Move the centroids to the average of their members
        for i in range(k):
            len_best = len(bestmatches[i])

            if len_best > 0:          
                for user_id in bestmatches[i]:
                    row = prefs[user_id]
                    for m in row:
                        centroids[i][m]+=row[m]
            for key in centroids[i].keys():
                centroids[i][key]/=len_best
                # We may have made the centroids quite dense which significantly
                # slows down subsequent iterations, so we delete values below a
                # threshold to speed things up
                if centroids[i][key] < 0.001:
                    del centroids[i][key]

    print bestmatches

    return centroids, bestmatches

def cluster_users(users):
	prefs = {}
	for user in users:
		prefs[user.id] = user.voting_history;

	centroids, bestmatches = kcluster(prefs, k=3, max_iterations=10) 

def main():
	#Testing clustering
	prefs = {0 : (1, 0, 0, 0), 1 : (0, 0, 0, 0), 2 : (1, 0, 2, 1), 3 : (1, 0, 2, 1), 4 : (1, 0, 2, 1)}
	c, b = kcluster(prefs, k=2)

	print c
	print b

if __name__ == '__main__':
	main()