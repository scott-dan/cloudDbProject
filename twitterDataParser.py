import json
import time
from datetime import datetime

inFile = 'Eurovision3'
outFile = inFile + '_clean' + '.json'

def main():
    tweets = []
    print("Scanning {} for tweets...\n".format(inFile))
    with open(inFile + '.json') as f_in:
        for line in f_in:
            if "created_at" not in line:
                continue
            else:
                tweet = json.loads(line)
                tweetObj = {
                    "created_at": tweet["created_at"],
                    "id": tweet["id"],
                    "text": tweet["text"],
                    "user": {
                        "id": tweet["user"]["id"],
                        "name": tweet["user"]["name"],
                        "screen_name": tweet["user"]["screen_name"],
                        "location": tweet["user"]["location"],
                        "verified": tweet["user"]["verified"]
                    },
                    "is_quote_status": tweet["is_quote_status"],
                    "hashtags": tweet["entities"]["hashtags"],
                    "timestamp_ms": tweet["timestamp_ms"],
                    "in_reply_to_status_id": tweet["in_reply_to_status_id"],
                    "in_reply_to_user_id": tweet["in_reply_to_user_id"],
                    "in_reply_to_screen_name": tweet["in_reply_to_screen_name"]
                }
                if "retweeted_status" in line:
                    tweetObj["retweeted_status_id"] = tweet["retweeted_status"]["id"]
                #print(tweetObj)
                clean_tweet = json.dumps(tweetObj)
                #print(clean_tweet)
                tweets.append(clean_tweet)
        #print(tweets[42069])
    f_in.close()
    
    
	#Will go back to writing out once data is properly formatted
    with open(outFile, "w", encoding = 'utf-8') as f_out:
        f_out.write('[')
        for tweet in tweets:
            f_out.write(tweet + ',\n')
        f_out.write(']')
    f_out.close()
    
    
if __name__ == "__main__":
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    start_time = time.time()
    main()
    print("Completed scan in %s seconds" % (time.time() - start_time))
