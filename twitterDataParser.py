import json
import time
from datetime import datetime

inFile = 'Eurovision3'
outFile = inFile + '_clean' + '.json'

class User:
    def __init__(self, user_id, user_name, screen_name):
        self.user_id = user_id
        self.user_name = user_name
        self.screen_name = screen_name

class In_reply_to:
    def __init__(self, status_id, user_id, screen_name):
        self.status_id = status_id
        self.user_id = user_id
        self.screen_name = screen_name

class Tweet:
    def __init__(self, created_at, tweet_id, text, user, in_reply_to, location, hashtags, timestamp):
        self.created_at = created_at
        self.tweet_id = tweet_id
        self.text = text
        self.user = user
        self.in_reply_to = in_reply_to
        self.location = location
        self.hashtags = hashtags
        self.timestamp = timestamp        
        #we can add more class variables as we need

def main():
    tweets = []    
    
    print("Scanning {} for tweets...\n".format(inFile))
    
    with open(inFile + '.json') as f_in:
        for line in f_in:
            if "created_at" not in line:
                continue
            else:
                dirtyData = json.loads(line)
                
                print(dirtyData["user"]["screen_name"])
                
                cleanData = Tweet(
                dirtyData["created_at"],
                dirtyData["id"],
                dirtyData["text"],
                User(dirtyData["user"]["id"],
                    dirtyData["user"]["name"],
                    dirtyData["user"]["screen_name"]
                    ),
                In_reply_to(dirtyData["in_reply_to_status_id"],
                    dirtyData["in_reply_to_user_id"],
                    dirtyData["in_reply_to_screen_name"]
                    ),
                dirtyData["user"]["location"], #should this be included in the User class instead?
                dirtyData["entities"]["hashtags"],
                dirtyData["timestamp_ms"]
                )                
                tweets.append(cleanData)
    f_in.close()
    
    
    with open(outFile, "w", encoding = 'utf-8') as f_out:
        f_out.write('[')
        for tweet in tweets:
            json.dump(tweet, ',')
        f_out.write(']')
    f_out.close()
    
    
if __name__ == "__main__":
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    start_time = time.time()
    main()
    print("Completed scan in %s seconds" % (time.time() - start_time))
    