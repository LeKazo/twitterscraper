import os
import pandas as pd
from datetime import date
today = date.today()
end_date = today
max_results = 10
search_term = 'Telsa'
from_date = '2019-01-01'
user_name = "elonmusk"
user_tweets = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-user '{user_name} until:{end_date}' > user-tweets.txt"
os.system(user_tweets)
if os.stat("user-tweets.txt").st_size == 0:
  print('No Tweets found')
else:
  df = pd.read_csv('user-tweets.txt', names=['content'])
  for row in df['content'].iteritems():
    print(row)
