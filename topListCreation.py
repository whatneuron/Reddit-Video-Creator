import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='Gv3YW3LSPq6-sA',
                     client_secret='b-UJkE642Y-kU4B0ce1_ySle_c8',
                     user_agent='Fun Script by /u/KinoZampie :)',
                     username='KinoZampie',
                     password='RedTheDit123$$')

postList = []
finalList = []
for submission in reddit.subreddit('askreddit').top("day"):
    postList.append(submission.url)

for link in postList:
    submission = reddit.submission(url=link)
    wordCount = 0
    if len(submission.title) < 85:
        for comment in submission.comments:
            if isinstance(comment, MoreComments):
                continue
            if len(comment.body) >= 200 and len(comment.body) <= 1200:
                wordCount = wordCount + len(comment.body)
            if wordCount >= 10000:
                finalList.append(link)
                break


file = open("redditList.txt", "w")
for x in finalList:
    file.write(x+"\n")
file.close()
