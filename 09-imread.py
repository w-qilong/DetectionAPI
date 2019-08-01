#
# FILENAME.
#       imread.py - OpenCV imread.
#
# FUNCTIONAL DESCRIPTION.
#       The app read an image file and analyze it.
#
# NOTICE.
#       Author: zhugy2@lenovo.com (Guang Yu Zhu)
#       Created on 2019/5/12
#

#
# Include standard packages.
#

import argparse
import logging
import pdb

#
# Include specific packages.
#

import cv2
import numpy as np
import matplotlib.pyplot as plt

#
# Build argument parser and return it.
#
    
def buildArgParser():

    parser = argparse.ArgumentParser(
                description='Build ...')
                
    #
    # Standard arguments
    #
                
    parser.add_argument(
            "-v", 
            dest="verbose", 
            action='store_true',    
            help="Verbose log") 
            
    #
    # Anonymous arguments.
    #
                
    parser.add_argument(
            'file',
            help='A file') 
            
    #
    # Specific arguments
    #     
    
    parser.add_argument(
            "-r", 
            type=int,
            default=10,
            dest="rate", 
            help="Rate between 0 ~ 100")   

    parser.add_argument(
            "--show", 
            dest="showDetail",
            action='store_true',             
            help="Show detail.")            

    return parser
    
def getHead(block, rate):

    #
    # Sort colors.
    #
    
    colors = block.flatten()
    colors.sort()
    
    #
    # Select colors.
    #    
    
    num = len(colors)
    logging.info('len(colors) = %d' % num)
    colors = colors[:int(num*(rate/100))]    
    logging.info('len(colors) = %d' % len(colors))    
    colors = np.unique(colors)
    logging.info('len(colors) = %d' % len(colors))    

    #
    # Get minPoints.
    #
    
    minPoints = []    
    for y in range(block.shape[0]):
        for x in range(block.shape[1]):
            if block[y][x] in colors:
                minPoints.append([y, x])
    logging.info('len(minPoints) = %d' % len(minPoints))    
    
    #
    # Get head.
    #
    
    yList = [p[0] for p in minPoints]        
    xList = [p[1] for p in minPoints]
    
    cx = -1
    cy = -1
    
    cx = int(sum(xList) / len(xList))
    cy = int(sum(yList) / len(yList))
    logging.info('head = (%d, %d)' % (cx, cy))
    
    return (cx, cy, minPoints)
    
def main():    

    #
    # Parse arguments
    #
    
    args = buildArgParser().parse_args()
    
    #
    # Enable log if -v
    #
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)

    #
    # Load the image.
    #
    
    img = cv2.imread(args.file)
    print('img.shape = %s' % str(img.shape))
    
    #
    # Convert it to gray colors.
    #
    
    img2 = img[:, :, 0].copy()
    print('img2.shape = %s' % str(img2.shape))
    cv2.imshow('img2', img)
    
    #pdb.set_trace()
    
    #
    # Show histogram.
    #
    
    hist = cv2.calcHist([img2], [0], None, [256], [0, 256])
    #print('hist = %s' % str(hist))
    
    if args.showDetail:
        plt.bar(range(1,257), hist)
        plt.show()    
        
    #
    # Get a head.
    #
    
    (cx, cy, minPoints) = getHead(img2, args.rate)
    
    
    #
    # Label head.
    #    
    
    for p in minPoints:
        cv2.circle(
            img,
            (p[1], p[0]), 
            4,
            (255, 0, 0),
            -1)    
            
    cv2.circle(
        img,
        (cx, cy), 
        4,
        (0, 0, 255),
        -1)              
            
    cv2.imshow('img', img)            
    
    #
    # Close windows.
    #
    
    #pdb.set_trace()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    main()