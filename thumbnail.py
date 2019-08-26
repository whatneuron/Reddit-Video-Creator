from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import os
import random


image = Image.new('RGB', (1920, 1080), "#19191A")

font = ImageFont.truetype('Arial Bold',175)
draw = ImageDraw.Draw(image)
draw.text((30, 30), str("r/AskReddit"), font=font, fill="#FF4401")
font = ImageFont.truetype("Arial Bold",100)
margin = 30
offset = 220
# for line in textwrap.wrap(str("submission.title"), width=65):
for line in textwrap.wrap(str("What is the best way to bring an arrogant person down a notch or two?"), width=20):
    draw.text((margin, offset), line, font=font, fill="#d7dadc")
    offset += font.getsize(line)[1]+5

image.save("0.png", "PNG")

background = Image.open("0.png")
foreground = Image.open("thumb/{}.png".format(str(random.randrange(1, 81))))

background.paste(foreground, (960, 0), foreground)
background.save("new.png")