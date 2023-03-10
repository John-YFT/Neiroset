import cv2
face_cascade=cv2.CascadeClassifier(r'C:\Users\John\Desktop\temp\classifier\cascade.xml')
img= cv2.imread(r'C:\Users\John\Desktop\temp\p\1588088953197.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray)
for(x,y,w,h) in faces:
    resized=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
