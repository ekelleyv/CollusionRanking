# class of posts for a social content website.  Posts can have bias.

import random

class Post(object):
    def __init__(self, post_bias, id, time):
        self.post_bias = post_bias  # bias of the post
        self.id = id                # id of the post
        self.time = time            # time of the post
