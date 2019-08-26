import praw
from praw.models import MoreComments
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import os
import sys

reddit = praw.Reddit(client_id='Gv3YW3LSPq6-sA',
                     client_secret='b-UJkE642Y-kU4B0ce1_ySle_c8',
                     user_agent='Fun Script by /u/KinoZampie :)',
                     username='KinoZampie',
                     password='RedTheDit123$$')
try:
    link = str(sys.argv[1])
except:
    link = input("Enter Reddit URL: ")

submission = reddit.submission(url=link)

#YT Video Stuff
title = submission.title


credit = "r/AskReddit {}\nCredits:\nPermalink: {}\nRedditors:\nu/{}\n".format(str(submission.title), link, str(submission.author))
os.mkdir(str(submission.title))
os.chdir(str(submission.title))

image = Image.new('RGB', (1920, 1080), "#19191A")

font = ImageFont.truetype('Arial',40)
draw = ImageDraw.Draw(image)
draw.text((30, 120), str(submission.author), font=font, fill="#d7dadc")
font = ImageFont.truetype("Arial Bold",60)
margin = 30
offset = 190
for line in textwrap.wrap(str(submission.title), width=65):
    draw.text((margin, offset), line, font=font, fill="#d7dadc")
    offset += font.getsize(line)[1]+5

image.save("0.png", "PNG")
file = open("sample.txt", "w")
file.write(str(submission.title))
file.close()
os.system("say -f sample.txt -v Daniel -o 0.aiff")
os.system("ffmpeg -loglevel quiet -loop 1 -i 0.png -i 0.aiff -q:v 5 -shortest 0.ts")
print("Done with: 0")

wordCount = 0
count = 0

for comment in submission.comments:
    if isinstance(comment, MoreComments):
        continue
    if len(comment.body) >= 200 and len(comment.body) <=1200 and wordCount <= 10000:
        count+=1
        wordCount = wordCount + len(str(comment.body))

        image = Image.new('RGB', (1920, 1080), "#19191A")

        font = ImageFont.truetype("Arial", 40)
        w, h = font.getsize(str(comment.author))

        draw = ImageDraw.Draw(image)
        credit = credit + "u/" +str(comment.author) + "\n"
        draw.text((30, 120), str(comment.author), font=font, fill="#4fbcff")
        draw.text((50 + w, 120), str(comment.score) + " points", font=font, fill="#818384")
        margin = 30
        offset = 190
        font = ImageFont.truetype("Arial", 47)
        for line in textwrap.wrap(str(comment.body), width=85):
            draw.text((margin, offset), line, font=font, fill="#d7dadc")
            offset += font.getsize(line)[1] + 5
        image.save(str(count)+".png", "PNG")
        file = open("sample.txt","w")
        file.write(str(comment.body))
        file.close()
        os.system("say -f sample.txt -v Daniel -o "+str(count)+".aiff")
        os.system("ffmpeg -loglevel quiet -loop 1 -i "+str(count)+".png -i "+str(count)+".aiff -q:v 5 -shortest "+str(count)+".ts")
        print("Done with: "+str(count))
command = 'ffmpeg -loglevel quiet -i "concat:'
for x in range(count+1):
    command = command + str(x) + ".ts|"

command = command[0:len(command)-1]+'"'
command = command + " -c copy final.ts"
print("Combining...")
os.system(command)
os.system("ffmpeg -loglevel quiet -i final.ts final.mp4")
os.system("ffmpeg -loglevel quiet -i 0.png thumb.jpg")
file = open("credit.txt", "w")
file.write(credit)
file.close()
os.system("rm -r *.png")
os.system("rm -r *.ts")
os.system("rm -r *.aiff")
os.system("rm -r sample.txt")
print("Done!")

#Auto YT Stuff

fileName = str(submission.title)+"/final.mp4"
description = credit
keywords = "r/AskReddit,askreddit,ask,reddit,reddit video,funny reddit"

os.chdir("..")
youtubeCommand = 'python3 YTredditVideo.py --file="{}" --title="{}" --description="{}" --keywords="{}"'.format(fileName, title, description, keywords)
os.system(youtubeCommand)

os.system("rm -r {}".format(submission.title))
