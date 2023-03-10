import cv2 
from matplotlib import pyplot as pltd 

xml_data = cv2.CascadeClassifier(r'C:\Users\John\Desktop\temp\classifier\cascade.xml') 
imaging = cv2.imread(r"C:\Users\John\Desktop\Documents\Ynic\4 semac\Neiroset\test\media\1.jpg") 
imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY) 
imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB) 
detecting = xml_data.detectMultiScale(imaging_gray) 
amountDetecting = len(detecting) 
if amountDetecting != 0: 
    for(a, b, width, height) in detecting: 
        cv2.rectangle(imaging_rgb,(a, b), 
                     (a + height, b + width),  
                     (0, 275, 0), 9) 

pltd.subplot(1, 1, 1) 
pltd.imshow(imaging_rgb) 
pltd.show() 
