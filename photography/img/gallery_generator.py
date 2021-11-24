import glob
import os

block = '''
<div class="mix col-xl-2 col-md-3 col-sm-4 col-6 p-0 {}">
    <a href="img/portfolio/{}/{}.jpg" class="portfolio-item img-popup set-bg" data-setbg="img/portfolio/{}/{}.jpg"></a>
</div>
'''

images = []

for group in os.listdir('./portfolio'):
    for file in glob.iglob('./portfolio/' + group + '/*.jpg'):
        images.append( (group, int(os.path.basename(file)[:-4])))

from pprint import pprint
images.sort(key=lambda x: x[1])

for group, image in images:
    print(block.format(group, group, image, group, image))
