import glob
import os
from PIL import Image
import random

block = '''
<a href="img/portfolio/{}"
data-pswp-width="{}"
data-pswp-height="{}"
target="_blank">
<img src="img/portfolio/thumbnail/{}" alt="" />
</a>
'''

images = []

for file in os.listdir('./portfolio'):
    if 'thumbnail' not in file:
        f = Image.open("portfolio/" + file)
        height,width = f.size

        images.append( (file, height, width) )


random.shuffle(images)

for image, height, width in images:
    print(block.format(image, width, height, image))
