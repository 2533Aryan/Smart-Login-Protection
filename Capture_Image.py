def camera_capture():

    import cv2

    camera = cv2.VideoCapture(0) #Captures the image and has port = 0
    for i in range(12):
        return_value, image = camera.read()
        cv2.imwrite('opencv'+str(i)+'.png', image)
    del(camera)
    
camera_capture()

