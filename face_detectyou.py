import cv2
import numpy as  np
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.videocapture(0)
id=raw_input('emter user id')
sampleNum=0
while(True):
	ret,img=cam.read()
	gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
	sampleNum=sampleNum+1
		cv2.imwrite("dataset/user."+str(id)+"."+str(sampleNum)+".jpg")
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.waitKey(100)
	cv2.imshow("face",img)
	cv2.waitKey(10)
	if(sampleNum>60):
		break
cam.release()
cv2.destroyAllWindows()
