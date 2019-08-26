import os
import praw

reddit = praw.Reddit(client_id='Gv3YW3LSPq6-sA',
                     client_secret='b-UJkE642Y-kU4B0ce1_ySle_c8',
                     user_agent='Fun Script by /u/KinoZampie :)',
                     username='KinoZampie',
                     password='RedTheDit123$$')

with open('redditList.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('redditList.txt', 'w') as fout:
    fout.writelines(data[1:])


try:
    if data[0][0:-1] == "":
        exit()
    os.system("python3 redditVideo.py {}".format(data[0][0:-1]))
except:
    pass
