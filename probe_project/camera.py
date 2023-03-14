import cv2
 
cam = cv2.VideoCapture(0)
cam.set(3,1280) #CV_CAP_PROP_FRAME_WIDTH
cam.set(4,720) #CV_CAP_PROP_FRAME_HEIGHT
#cam.set(5,0) #CV_CAP_PROP_FPS
 
while True:
    ret_val, img = cam.read() # 캠 이미지 불러오기
 
    cv2.imshow("Cam Viewer",img) # 불러온 이미지 출력하기
    if cv2.waitKey(1) == 27:
        break  # esc to quit