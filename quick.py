import os

for x in range(1,81):
    woahname = str(x)+'.png'
    fname = str(x)+".png"
    os.system("convert thumb/{} -resize 960x10000 thumb/{}".format(fname,fname))
    fname = str(x) + ".jpg"
    os.system("convert thumb/{} -resize 960x10000 thumb/{}".format(fname, woahname))
    print("Done with {}".format(x))