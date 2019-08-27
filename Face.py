// Reading the images with Python
 def read_images ( path , sz = None ):
c = 0
X ,y = [] , []
for dirname , dirnames , filenames in os . walk ( path ):
for subdirname in dirnames :
subject_path = os . path . join ( dirname , subdirname )
for filename in os . listdir ( subject_path ):
try :
im = Image . open ( os . path . join ( subject_path , filename ))
im = im . convert ("L")
# resize to given size (if given )
if ( sz is not None ) :
im = im . resize (sz , Image . ANTIALIAS )
X. append ( np . asarray (im , dtype = np . uint8 ) )
y. append (c)
except IOError :
print "I/O error ({0}) : {1} ". format ( errno , strerror )
except :
print " Unexpected error :", sys . exc_info () [0]
raise
c = c +1
return [X , y]
//FACE DETECTION:
clear all
clc
%Detect objects using Viola-Jones Algorithm
%To detect Face
FDetect = vision.CascadeObjectDetector;
%Read the input image
I = imread('HarryPotter.jpg');
%Returns Bounding Box values based on number of objects
BB = step(FDetect,I);
figure,
imshow(I); hold on
for i = 1:size(BB,1)
 rectangle('Position',BB(i,:),'LineWidth',5,'LineStyle','-
','EdgeColor','r');
end
title('Face Detection');
hold off;
//NOSE DETECTION:
%To detect Nose
NoseDetect = vision.CascadeObjectDetector('Nose','MergeThreshold',16);
BB=step(NoseDetect,I);
figure,
imshow(I); hold on
for i = 1:size(BB,1)
 rectangle('Position',BB(i,:),'LineWidth',4,'LineStyle','-
','EdgeColor','b');
end
title('Nose Detection');
hold off;
//MOUTH DETECTION:
%To detect Mouth
MouthDetect = vision.CascadeObjectDetector('Mouth','MergeThreshold',16);
BB=step(MouthDetect,I);
figure,
imshow(I); hold on
for i = 1:size(BB,1)
rectangle('Position',BB(i,:),'LineWidth',4,'LineStyle','-
','EdgeColor','r');
end
title('Mouth Detection');
hold off;
//EYE DETECTION:
%To detect Eyes
EyeDetect = vision.CascadeObjectDetector('EyePairBig');
%Read the input Image
I = imread('harry_potter.jpg');
BB=step(EyeDetect,I);
figure,imshow(I);
rectangle('Position',BB,'LineWidth',4,'LineStyle','-','EdgeColor','b');
title('Eyes Detection');
Eyes=imcrop(I,BB);
figure,imshow(Eyes);
