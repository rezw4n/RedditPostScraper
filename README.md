# RedditPostScraper

`pyreddit` is a small python package that uses `Pushshift` API instead of `PRAW` that lets user to download whole subreddit or the amount of posts you need to download instead of top 500 posts.

# Requirements

pyreddit has two main dependencies. `pandas` for reading & writing data and `requests` getting the data from pushshift API.
In order to install them simply run this following command on your terminal:
`pip install pandas, requests`

# Quickstart

To use py reddit move the pyreddit folder to the place where you're working. Then start scripting. Here's an example of how you can use it:

```
from pyreddit.reddit import RedditScraper

# First you need to create an instance of  RedditScraper that takes two argument. First is the name of the subreddit which is s string and the second one is the number of post you'd like to scrape.
subreddit = RedditScraper('worldnews', 2000)

# Scraping latest 2000 titles of the posts in worldnews subreddit in a csv format
subreddit.scrape_title()

# Scraping all available data of latest 2000 posts in worldnews subreddit in a csv format
subreddit.scrape_subreddit()
```
