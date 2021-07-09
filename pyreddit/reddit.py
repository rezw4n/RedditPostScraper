import requests
from datetime import datetime
from os.path import isfile
import pandas as pd


class RedditScraper:
    def __init__(self, subreddit, number_of_post):
        self.subreddit = subreddit
        self.number_of_post = number_of_post

    def fetch_data(self, date):
        try:
            url = f"https://api.pushshift.io/reddit/submission/search?limit=1000&sort=desc&subreddit={self.subreddit}&before={str(date)}"
            return requests.get(url).json()
        except requests.exceptions.ConnectionError:
            return "Please make sure that you are connected to the internet and try again."

    def scrape_title(self):
        date = int(datetime.utcnow().timestamp())
        post_count = 0
        while post_count < self.number_of_post:
            data = self.fetch_data(date)

            if len(data) == 0:
                print(
                    f"The subreddit doesn't have any more posts to scrape.\n Finished scraping {post_count} post titles from {self.subreddit}")
                break

            titles = [post["title"] for post in data['data']]

            with open(f'{self.subreddit}_scraped_post_title.txt', 'a', encoding="utf-8") as file:
                file.write('\n'.join(titles) + '\n')

            date = data['data'][- 1]['created_utc']
            post_count += 100
            print(f"Scraped {post_count} post titles from {self.subreddit}")
        return f"Finished scraping {post_count} post titles from {self.subreddit}"

    def scrape_subreddit(self):
        date = int(datetime.utcnow().timestamp())
        post_count = 0
        while post_count < self.number_of_post:
            data = self.fetch_data(date)

            if len(data) == 0:
                print(
                    f"The subreddit doesn't have any more posts to scrape.\n Finished scraping {post_count} post titles from {self.subreddit}")
                break

            df = pd.DataFrame(data['data'])

            if not isfile(f'{self.subreddit}.csv'):
                df.to_csv(f'{self.subreddit}.csv')
            else:
                df.to_csv(f'{self.subreddit}.csv', mode='a', header=False)

            date = data['data'][- 1]['created_utc']
            post_count += 100
            print(f"Scraped {post_count} posts from {self.subreddit}")
        return f"Finished scraping {post_count} posts from {self.subreddit}"
