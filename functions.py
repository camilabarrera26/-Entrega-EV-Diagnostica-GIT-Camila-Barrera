import pandas as pd
from collections import Counter
import operator
import re

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

def most_tweets_day(data):
    dates = []
    for date in data["date"]:
        dates.append(date.date())
    dates_count = dict(Counter(dates))
    sorted_dates_count = dict(sorted(dates_count.items(), key=operator.itemgetter(1), reverse=True))
    count = 0
    for i in sorted_dates_count:
        if count == 10:
            break
        print(i)
        count += 1

def most_used_hashtag(data):
    content = []
    for contents in data["content"]:
        content.append(contents)
    hashtags = []
    for i in range(0, len(content)):
        hashtag = re.findall(r'#(\w+)', content[i])
        for h in hashtag:
            hashtags.append(h)
    hashtags_count = dict(Counter(hashtags))
    sorted_hashtags_count = dict(sorted(hashtags_count.items(), key=operator.itemgetter(1), reverse=True))
    count = 0
    for i in sorted_hashtags_count:
        if count == 10:
            break
        print(i)
        count += 1