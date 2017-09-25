import json
import fileinput
import sys

retweeted = []
for line in fileinput.input(sys.argv[1]):
    tweet = json.loads(line)
    retweeted.append(tweet)

top_retweeted = sorted(retweeted, key=lambda x: x[
                       'retweet_count'], reverse=True)

for t in top_retweeted[:10]:
    print("{:,} https://twitter.com/{}/status/{}".format(
        int(t['retweet_count']), str(t['user']['screen_name']), str(t['id'])))

with open("data/processed/retweets_original_tweet.txt", "w") as f:
    f.write(json.dumps(top_retweeted[0]))
