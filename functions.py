import pandas as pd

def most_retweeted(data):
    sorted = data.sort_values(by=['retweetCount'], ascending=False)
    print(sorted.head(10))
