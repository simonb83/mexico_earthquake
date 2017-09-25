import dateutil.parser
import numpy as np
import fileinput
import sys
import json


with open("data/processed/retweets_original_tweet.txt", "r") as f:
    original_tweet = json.loads(f.read())

original_tweet_id = original_tweet['id']
original_tweet_time = dateutil.parser.parse(original_tweet['created_at'])

tweet_diffs = []
for line in fileinput.input(sys.argv[1]):
    tweet = json.loads(line)
    if "retweeted_status" in tweet.keys():
        if original_tweet_id == tweet['retweeted_status']['id']:
            tweet_time = dateutil.parser.parse(tweet['created_at'])
            hours_after = (tweet_time - original_tweet_time).total_seconds() / 3600
            hours_after = round(hours_after, 1)
            tweet_diffs.append(hours_after)

# max_val = int(np.ceil(np.max(tweet_diffs) / 6))
# bins = list(range(0, 6*max_val, 6))
# hist, bins = np.histogram(tweet_diffs, bins)
# hist = hist / len(tweet_diffs)

# data = []
# for x, y in zip(hist, bins[1:]):
#     data.append({'name': str(y), 'value': x})

# print(json.dumps(data))

print(json.dumps(tweet_diffs))
