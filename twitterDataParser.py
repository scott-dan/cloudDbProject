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
				clean_tweet = [
				'{' + "created_at" + ':' + tweet["created_at"],
				"id" + ':' + tweet["id_str"],
				"text" + ':' + tweet["text"],
					"user" + ':' + '{' +
					"id" + ':' + tweet["user"]["id_str"], #concat or comma?
					"name" + ':' + tweet["user"]["name"],
					"screen_name" + ':' + tweet["user"]["screen_name"],
					#"location" + ':' + tweet["user"]["location"] + '}', #Need to check for null and still insert in user section
				#"hashtags" + ':' + tweet["entities"]["hashtags"], #I need to figure out how to represent this list
				"timestamp_ms" + ':' + tweet["timestamp_ms"]
				]
				if(tweet["in_reply_to_status_id"]):
					clean_tweet.append("in_reply_to_status_id" + ':' + tweet["in_reply_to_status_id_str"])
				if(tweet["in_reply_to_user_id"]):
					clean_tweet.append("in_reply_to_user_id" + ':' + tweet["in_reply_to_user_id_str"])
				if(tweet["in_reply_to_screen_name"]):
					clean_tweet.append("in_reply_to_screen_name" + ':' + tweet["in_reply_to_screen_name"])
				clean_tweet.append('}')
			tweets.append(clean_tweet)
		print(tweets[42069])
	f_in.close()
    
    
	#Will go back to writing out once data is properly formatted
    #with open(outFile, "w", encoding = 'utf-8') as f_out:
    #    f_out.write('[')
    #    for tweet in tweets:
    #        json.dump(tweet, ',')
    #    f_out.write(']')
    #f_out.close()
    
    
if __name__ == "__main__":
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    start_time = time.time()
    main()
    print("Completed scan in %s seconds" % (time.time() - start_time))
    
