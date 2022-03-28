import pandas as pd
from collections import Counter
import operator

def most_retweeted(data):
    sorted = data.sort_values(by=['retweetCount'], ascending=False)
    print(sorted.head(10))

def most_tweets_user(data):
    users = []
    for user in data["user"]:
        users.append(user["username"])
    users_count = dict(Counter(users))
    sorted_users_count = dict(sorted(users_count.items(), key=operator.itemgetter(1), reverse=True))
    count = 0
    for i in sorted_users_count:
        if count == 10:
            break
        print(i)
        count += 1