#Simply Reddit TUI pretty self-explanatory code

import praw
import os

os.system('clear')

#Basically used by the praw api to authenticate to reddit
reddit = praw.Reddit(client_id='SM-xXY6ho0CGMIHP1nDv9g', client_secret='Q3uxDAEJfabCeyMbKz6ZaxlSmNtcSA', user_agent='webScraper')

#Fetches and prints the title of the top 5 post in the whole of reddit

subred = input('Please enter the subreddit you wanna see | ')

try:
    hottestPosts = reddit.subreddit(subred).hot(limit=5)

    for post in hottestPosts:
        print('Subreddit - ' , subred)
        print('Title - ' ,post.title)
        print('User - ' ,post.author)
        print('------------------')

    print(f'To see more, check out https://www.reddit.com/r/{subred}')

except:
    print('An error occured, the subreddit was not found #404')

#EOP somehow
