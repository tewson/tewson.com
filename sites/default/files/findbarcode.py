#!/usr/bin/python
# This is a standalone program. Pass an image name as a first parameter of the program.

import sys
import Image
from math import sin,cos,tan,acos,asin,atan,floor,pi
from opencv.cv import *
from opencv.highgui import *

# toggle between CV_HOUGH_STANDARD and CV_HOUGH_PROBILISTIC
USE_STANDARD=1

def detectLines(src,slopeThresholds = []):

    size = cvGetSize(src)
    
    dst = cvCreateImage( size, 8, 1 );
    color_dst = cvCreateImage( size, 8, 3 );
    
    storage = cvCreateMemStorage(0);
    lines = 0;
    cvCanny( src, dst, 50, 200, 3 );
    cvCvtColor( dst, color_dst, CV_GRAY2BGR );

    if USE_STANDARD:
        lines = cvHoughLines2( dst, storage, CV_HOUGH_STANDARD, 1, CV_PI/180, 90, 0, 0 );
        
        angles = []
        points = []
        for i in range(min(lines.total, 100)):
            line = lines[i]
            rho = line[0];
            theta = line[1];
            pt1 = CvPoint();
            pt2 = CvPoint();
            a = cos(theta);
            b = sin(theta);
            x0 = a*rho 
            y0 = b*rho
            pt1.x = cvRound(x0 + 1000*(-b));
            pt1.y = cvRound(y0 + 1000*(a));
            pt2.x = cvRound(x0 - 1000*(-b));
            pt2.y = cvRound(y0 - 1000*(a));
            
            try:
                #slope = abs(float(pt2.y)-pt1.y)/abs(pt2.x-pt1.x)
                slope = (float(pt2.y)-pt1.y)/(pt2.x-pt1.x)
            except:
                slope = 10000
            
            angle = atan(slope)
            #if angle < 0:
              #angle = angle+pi
            
            angles.append(angle)
            """
            print "slope = ",
            print slope
            print angle
            """
            if len(slopeThresholds) == 0 :
                cvLine( color_dst, pt1, pt2, CV_RGB(255,0,0), 3, 8 )
                points.append([pt1,pt2])
            else:
                mindesiredslope = slopeThresholds[0]
                maxdesiredslope = slopeThresholds[1]
                if mindesiredslope <= slope and slope <= maxdesiredslope:
                    cvLine( color_dst, pt1, pt2, CV_RGB(255,0,0), 3, 8 )
                    points.append([pt1,pt2])
            
    else:
        lines = cvHoughLines2( dst, storage, CV_HOUGH_PROBABILISTIC, 1, CV_PI/180, 60, 50, 10 );
        angles = []
        for line in lines:
            try:
                slope = abs(float(line[1].y)-line[0].y)/abs(line[1].x-line[0].x)
            except:
                slope = 10000
            #print "slope = ",
            #print slope
            #print atan(slope)
            angles.append(atan(slope))
            cvLine( color_dst, line[0], line[1], CV_RGB(255,0,0), 3, 8 );
    
    cvNamedWindow( "Source", 1 );
    cvShowImage( "Source", src );
    
    cvNamedWindow( "Dest", 1 );
    cvShowImage( "Dest", dst );

    cvNamedWindow( "Hough", 1 );
    cvShowImage( "Hough", color_dst );
    
    cvWaitKey(0)
    
    #all line angles
    return angles, points



if __name__ == "__main__":
    filename = "smallbarcode.jpg"
    if len(sys.argv)>1:
        filename = sys.argv[1]

    im = Image.open(filename)
    if im.size[1] < 700:
        im = im.resize((im.size[0]*700/im.size[1], 700), Image.BICUBIC)
        im.save(filename)
    
    src=cvLoadImage(filename,0);
    if not src:
        print "Error opening image %s" % filename
        sys.exit(-1)

    size = cvGetSize(src)   

    angles,points = detectLines(src)
    
    #print angles

    #quantize angles to 10 levels
    normalizer = float(max(angles) - min(angles))/559
    """
    print "max : ",
    print max(angles)
    print "min : ",
    print min(angles)
    """
    levels = list([] for i in range(560))
    #print levels
    
    for i in range(len(angles)):
      if normalizer == 0:
          quantized = 1
      else:
          quantized = int(floor((angles[i]-min(angles))/normalizer))
      #print angles[i],
      #print "quantized to ",
      #print quantized
      
      levels[quantized].append(angles[i])

    #sort quantized levels by population
    for i in range(len(levels)):
      for j in range(i):
        if len(levels[i]) > len(levels[j]):
          temp = levels[i]
          levels[i] = levels[j]
          levels[j] = temp

    rotate = sum(levels[0])/len(levels[0])
    
    im = Image.open(filename)
    #rotateangle = 90-rotate/pi*180
    rotateangle = rotate/pi*180 - 90
    
    print "original rotate angle : ",
    print rotate/pi*180,
    print " degree"
    print "rotate angle : ",
    print rotateangle,
    print " degree"
    
    out = im.rotate(rotateangle,Image.BICUBIC)
    
    #how to get rid of black pixels filled by rotation? b/c if the angle were small, these filled pixels could look like a line
    #crop in for 3 pixels to get rid of those filled pixels
    out = out.crop((3,3,im.size[0]-3,im.size[1]-3))
    
    out.save('temp.jpg')
    
    temp = cvLoadImage('temp.jpg',0)
    size = cvGetSize(temp)
    #cvNamedWindow( "Temp", 1 );
    #cvShowImage( "Temp", temp );
    erodedTemp = cvCreateImage(size,8,1)
    
    angles,points = detectLines(temp)
    
    element = cvCreateStructuringElementEx(21,1,10,0,CV_SHAPE_RECT)
    cvErode(temp,erodedTemp,element,1)
    
    allowedError = 0.01
    
    #normalize angles
    for i in range(len(angles)):
      if angles[i] < 0:
        angles[i] = angles[i] + pi/2
    
    print "min angle:",
    print min(angles)/pi*180
    print "max angle:",
    print max(angles)/pi*180
    horizontalLineAngles, horizontalLinePoints = detectLines(erodedTemp,[tan(min(angles))-allowedError,tan(min(angles))+allowedError])
    verticalLineAngles, verticalLinePoints = detectLines(temp,[tan(max(angles))-allowedError,tan(max(angles))+allowedError])

    #find leftmost x and rightmost x
    leftmostX = size.width
    rightmostX = 0
    for i in range(len(verticalLinePoints)):
        if leftmostX > verticalLinePoints[i][0].x:
            leftmostX = verticalLinePoints[i][0].x
        if rightmostX < verticalLinePoints[i][0].x:
            rightmostX = verticalLinePoints[i][0].x
    #erodedTempAngles,erodeTempPoints = detectLines(erodedTemp,[tan(min(angles))-allowedError,tan(min(angles))+allowedError])
    
    temp = cvLoadImage('temp.jpg')
    
    leftmostPt1 = CvPoint()
    leftmostPt1.x = leftmostX
    leftmostPt1.y = 0
    leftmostPt2 = CvPoint()
    leftmostPt2.x = leftmostX
    leftmostPt2.y = size.height
    
    rightmostPt1 = CvPoint()
    rightmostPt1.x = rightmostX
    rightmostPt1.y = 0
    rightmostPt2 = CvPoint()
    rightmostPt2.x = rightmostX
    rightmostPt2.y = size.height
    
    for i in range(len(horizontalLinePoints)):
        for j in range(i):
            if(horizontalLinePoints[i][0].y < horizontalLinePoints[j][0].y):
                tmppt = horizontalLinePoints[i][0]
                horizontalLinePoints[i][0] = horizontalLinePoints[j][0]
                horizontalLinePoints[j][0] = tmppt
                
                tmppt = horizontalLinePoints[i][1]
                horizontalLinePoints[i][1] = horizontalLinePoints[j][1]
                horizontalLinePoints[j][1] = tmppt
    
    #define grid
    cvLine( temp, leftmostPt1, leftmostPt2, CV_RGB(255,0,0), 3, 8 )
    cvLine( temp, rightmostPt1, rightmostPt2, CV_RGB(255,0,0), 3, 8 )
    for pts in horizontalLinePoints:
        cvLine( temp, pts[0], pts[1], CV_RGB(255,0,0), 3, 8 )
    #"""
    cvNamedWindow( "afterRotation",1);
    cvShowImage( "afterRotation", temp);
    
    cvWaitKey(0)
    
    temp = cvLoadImage('temp.jpg',0)
    #"""
    #crop regions
    padding = 10
    maxCroppedRegionLines = 0
    maxCroppedRegionXY = []
    for i in range(len(horizontalLinePoints)-1):
        croppingWidth = rightmostX - leftmostX + 2*padding
        croppingHeight = abs(horizontalLinePoints[i+1][0].y - horizontalLinePoints[i][0].y)
        
        #in case that it's beyond boundaries
        if(leftmostX - padding < 0):
            croppingWidth = croppingWidth + leftmostX - padding
            leftmostX = padding
        """
        print "cropping from (",
        print leftmostX - padding,
        print ",",
        print horizontalLinePoints[i][0].y,
        print ") to (",
        print rightmostX + padding,
        print ",",
        print horizontalLinePoints[i+1][0].y,
        print ")"
        print "width ",
        print croppingWidth
        print "height ",
        print croppingHeight
        print leftmostX
        print horizontalLinePoints[i][0].y
        """
        cropped = cvCreateImage(cvSize(croppingWidth,croppingHeight),8,1)
        
        #print "cvGetSubRect(temp,cvRect("+str(leftmostX - padding)+","+str(horizontalLinePoints[i][0].y)+","+str(croppingWidth)+","+str(croppingHeight)+"))"
        svc_region = cvGetSubRect(temp,cvRect(leftmostX - padding,horizontalLinePoints[i][0].y,croppingWidth,croppingHeight))
        cvCopy(svc_region,cropped)
        """
        cvNamedWindow( "Crop"+str(i),1);
        cvShowImage( "Crop"+str(i), cropped);
        """
        #consider only large region by ratio
        if (croppingWidth / croppingHeight) < 50:
            #count lines
            croppedLineAngles, croppedLinePoints = detectLines(cropped)
            croppedLines = len(croppedLineAngles)
            #print "-----------------------------lines here: ",
            if maxCroppedRegionLines < croppedLines:
                maxCroppedRegionLines = croppedLines
                maxCroppedRegionXY = [[leftmostX,horizontalLinePoints[i][0].y],[rightmostX,horizontalLinePoints[i+1][0].y]]
                selectedCrop = cropped

    #cvWaitKey(0)
    
    #display result
    temp = cvLoadImage('temp.jpg')
    
    
    
    borderPt1 = CvPoint()
    borderPt1.x = maxCroppedRegionXY[0][0] - padding
    borderPt1.y = maxCroppedRegionXY[0][1] - padding
    borderPt2 = CvPoint()
    borderPt2.x = maxCroppedRegionXY[1][0] #+ padding
    borderPt2.y = maxCroppedRegionXY[1][1] #+ padding
    
    if borderPt1.x < 0: borderPt1.x = 0
    if borderPt1.y < 0: borderPt1.y = 0
    
    #cvLine( temp, leftmostPt1, leftmostPt2, CV_RGB(255,0,0), 3, 8 )
    #cvLine( temp, rightmostPt1, rightmostPt2, CV_RGB(255,0,0), 3, 8 )
    
    cvRectangle(temp,borderPt1,borderPt2,CV_RGB(255,0,0))
    #"""
    
    cvNamedWindow( "toClassify",1);
    cvShowImage( "toClassify", selectedCrop);
    
    cvWaitKey(0)
    #"""
    """
    cvNamedWindow( "Final",1);
    cvShowImage( "Final", temp);
    
    cvWaitKey(0)
    """
    
    """
    #closing morph
    cropSize = cvGetSize(selectedCrop)
    erode = cvCreateImage(cropSize,8,1)
    dilate = cvCreateImage(cropSize,8,1)
    sub = cvCreateImage(cropSize,8,1)
    
    element = cvCreateStructuringElementEx(1,20,0,10,CV_SHAPE_RECT)
    
    cvDilate(selectedCrop,dilate,element,1)
    cvErode(dilate,erode,element,1)
    
    cvSub(erode,selectedCrop,sub)
    
    cvNamedWindow("selectedCrop",1)
    cvShowImage("selectedCrop",selectedCrop)

    cvNamedWindow("dilate",1)
    cvShowImage("dilate",dilate)

    cvNamedWindow("erode",1)
    cvShowImage("erode",erode)

    cvNamedWindow("sub",1)
    cvShowImage("sub",sub)
    """
    
    cropSize = cvGetSize(selectedCrop)
    erode = cvCreateImage(cropSize,8,1)
    dilate = cvCreateImage(cropSize,8,1)
    sub = cvCreateImage(cropSize,8,1)
    
    element = cvCreateStructuringElementEx(1,21,0,10,CV_SHAPE_RECT)
    
    cvDilate(selectedCrop,dilate,element,1)
    cvErode(dilate,erode,element,1)
    
    cvThreshold(selectedCrop,selectedCrop, 200, 255, CV_THRESH_BINARY);
    cvThreshold(erode,erode, 200, 255, CV_THRESH_BINARY);
    
    cvSub(erode,selectedCrop,sub)
    #"""
    cvNamedWindow("selectedCrop",1)
    cvShowImage("selectedCrop",selectedCrop)

    cvNamedWindow("dilate",1)
    cvShowImage("dilate",dilate)

    cvNamedWindow("erode",1)
    cvShowImage("erode",erode)

    cvNamedWindow("sub",1)
    cvShowImage("sub",sub)
    
    cvWaitKey(0)
    #"""
    #save the difference image
    cvSaveImage("diff.bmp",sub)
    #start counting errors
    #we consider the 1x2 white block
    diff = Image.open("diff.bmp")
    pixels = diff.load()
    errCount = 0
    print "size: "+str(diff.size)
    for y in range(diff.size[1]):
        for x in range(diff.size[0]):
            #print "at ("+str(x)+","+str(y)+")"
            #print pixels[(x,y)]
            if x < (diff.size[0]-1):
                if pixels[(x,y)] == 255 and pixels[(x+1,y)] == 255:
                    errCount = errCount + 1
                    x = x + 1
    
    print "error: "+str(errCount)
