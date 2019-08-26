from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap

# user = "bobthebuilder"
#
# score = "20203"
#
# content = "After the tour when people are allowed to roam the grounds, I hear his mom screaming and look over to the barn and this kid has climbed the fence into the field with our long horn oxen and is trying to poke them with a stick. I walk over and calmly told him to get out of the field before our lazy oxen decide they've had enough, but this jack off decides to look me in the eye and smack Ted on the ass with the stick like it's a riding crop. Ted, bless him, just kinda jumps a little and whips his head around with a WTF dude look on his face. But seeing as he's a long horn, he just wipes this kid out with one of his horns when he turned his head. Kid goes flying into the dirt and is having a melt down. Mom is freaking out. I'm like dude, get the hell out of the pen before Ted actually gets mad. I'm like dude, get the hell out of the pen before Ted actually gets mad. I'm like dude, get the hell out of the pen before Ted actually gets mad. I'm like dude, get the hell out of the pen before Ted actually gets mad. I'm like dude, get the hell out of the pen before Ted actually gets mad. I'm like dude, get the hell out of the pen before Ted actually gets mad. "
# print(len(content))
#
# image = Image.new('RGB', (1920, 1080), "#19191A")
#
# font = ImageFont.truetype("Arial",40)
# w,h = font.getsize(user)
#
# draw = ImageDraw.Draw(image)
#
# draw.text((30,120),user,font=font,fill="#4fbcff")
# draw.text((50+w,120),score+" points",font=font,fill="#818384")
# margin = 30
# offset = 190
# font = ImageFont.truetype("Arial",47)
# for line in textwrap.wrap(content, width=85):
#     draw.text((margin, offset), line, font=font, fill="#d7dadc")
#     offset += font.getsize(line)[1]+5
#
# image.save("image.png", "PNG")


title = "What is the craziest drink you've is the craziest drink you've is the craziest drink you've had?"
user = "Nope"
image = Image.new('RGB', (1920, 1080), "#19191A")

font = ImageFont.truetype('Arial',40)

draw = ImageDraw.Draw(image)
draw.text((30, 120), user, font=font, fill="#d7dadc")

font = ImageFont.truetype("Arial Bold",60)
margin = 30
offset = 190
for line in textwrap.wrap(title, width=65):
    draw.text((margin, offset), line, font=font, fill="#d7dadc")
    offset += font.getsize(line)[1]+5

image.save("0.png", "PNG")
