# coding: utf-8

'''
Testing tools for svg conversion
'''

import time
from cairosvg import svg2png
import os

import logging
logging.basicConfig(format='%(asctime)s %(message)s')

# source svg files for testing
FILES_DIR ='../tmp/'

def test():
    svgfiles = [f for f in os.listdir(FILES_DIR) if f.endswith('.svg')]
    for f in svgfiles:
        t0 = time.time()
        svg2png(url = FILES_DIR + f, write_to = FILES_DIR + f.replace('.svg', '.png'))
        tf = time.time()
        logging.warning('Finito %s file (%s secs)', f , tf-t0)


if __name__ == '__main__':
    test()